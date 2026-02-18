from __future__ import annotations

import hashlib
import json
import sqlite3
import threading
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel, Field

from backend.scrapers.bayer_ua_dekalb import BayerUADekalbScraper

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DB_PATH = DATA_DIR / "catalog.db"
FALLBACK_PATH = ROOT / "frontend" / "public" / "catalog_fallback.json"

app = FastAPI(title="Parostok Catalog API")


class UpdateRequest(BaseModel):
    markets: list[str] = Field(default_factory=lambda: ["UA", "US"])
    sources: list[str] = Field(default_factory=lambda: ["bayer_ua_dekalb", "bayer_us_dekalb"])
    dry_run: bool = False


@dataclass
class SourceStatus:
    id: str
    market: str
    enabled: bool
    reason: str | None
    last_run: str | None
    fields: list[str]


RUNS: dict[str, dict[str, Any]] = {}
LOCK = threading.Lock()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def get_conn() -> sqlite3.Connection:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with get_conn() as conn:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS hybrids(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              crop TEXT NOT NULL,
              name TEXT NOT NULL,
              brand TEXT,
              market TEXT NOT NULL,
              source_url TEXT NOT NULL,
              last_seen TEXT NOT NULL,
              last_updated TEXT NOT NULL,
              UNIQUE(name, market, source_url)
            );
            CREATE TABLE IF NOT EXISTS attributes(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              hybrid_id INTEGER NOT NULL,
              key TEXT NOT NULL,
              value TEXT,
              evidence TEXT,
              evidence_hash TEXT,
              selector TEXT,
              source_url TEXT NOT NULL,
              extracted_at TEXT NOT NULL,
              FOREIGN KEY(hybrid_id) REFERENCES hybrids(id)
            );
            CREATE TABLE IF NOT EXISTS runs(
              job_id TEXT PRIMARY KEY,
              started_at TEXT NOT NULL,
              finished_at TEXT,
              status TEXT NOT NULL,
              logs_json TEXT NOT NULL,
              counts_json TEXT NOT NULL
            );
            """
        )


def source_registry() -> list[SourceStatus]:
    return [
        SourceStatus(
            id="bayer_ua_dekalb",
            market="UA",
            enabled=True,
            reason=None,
            last_run=None,
            fields=[
                "name",
                "fao",
                "grain_type",
                "maturity_group",
                "advantages_text",
                "positioning.*",
                "density.*",
                "rating.*",
            ],
        ),
        SourceStatus(
            id="bayer_us_dekalb",
            market="US",
            enabled=False,
            reason="Network scraping not configured in this starter; use manual import.",
            last_run=None,
            fields=["name", "relative_maturity", "trait_package"],
        ),
    ]


def read_catalog() -> dict[str, Any]:
    with get_conn() as conn:
        hybrids = conn.execute("SELECT * FROM hybrids ORDER BY crop, name").fetchall()
        out: dict[str, list[dict[str, Any]]] = {}
        for h in hybrids:
            attrs = conn.execute(
                "SELECT key, value, evidence, evidence_hash, selector, source_url, extracted_at FROM attributes WHERE hybrid_id=?",
                (h["id"],),
            ).fetchall()
            out.setdefault(h["crop"], []).append(
                {
                    "id": h["id"],
                    "name": h["name"],
                    "brand": h["brand"],
                    "market": h["market"],
                    "source_url": h["source_url"],
                    "last_seen": h["last_seen"],
                    "last_updated": h["last_updated"],
                    "attributes": [dict(a) for a in attrs],
                }
            )
        return {"crops": out}


def write_fallback() -> None:
    FALLBACK_PATH.parent.mkdir(parents=True, exist_ok=True)
    FALLBACK_PATH.write_text(json.dumps(read_catalog(), indent=2), encoding="utf-8")


def persist_run(job_id: str, run: dict[str, Any]) -> None:
    with get_conn() as conn:
        conn.execute(
            """INSERT OR REPLACE INTO runs(job_id, started_at, finished_at, status, logs_json, counts_json)
               VALUES(?,?,?,?,?,?)""",
            (
                job_id,
                run["started_at"],
                run.get("finished_at"),
                run["status"],
                json.dumps(run["step_logs"]),
                json.dumps(run["counts"]),
            ),
        )


def run_update(job_id: str, req: UpdateRequest) -> None:
    with LOCK:
        run = RUNS[job_id]
    logs = run["step_logs"]

    def log(msg: str) -> None:
        logs.append({"time": utc_now(), "message": msg})
        persist_run(job_id, run)

    log("Starting catalog sync job.")
    enabled_sources = [s for s in source_registry() if s.id in req.sources and s.enabled]
    disabled_sources = [s for s in source_registry() if s.id in req.sources and not s.enabled]

    if disabled_sources:
        for src in disabled_sources:
            log(f"Source {src.id} disabled: {src.reason}")

    if not enabled_sources:
        run["status"] = "completed"
        run["finished_at"] = utc_now()
        log("No enabled sources. Nothing fetched.")
        persist_run(job_id, run)
        write_fallback()
        return

    for src in enabled_sources:
        if src.id != "bayer_ua_dekalb":
            log(f"Source {src.id} currently has no scraper implementation.")
            continue
        try:
            log("Fetching bayer_ua_dekalb start page.")
            scraper = BayerUADekalbScraper()
            result = scraper.run()
            run["counts"]["discovered"] += len(result["product_urls"])
            log(f"Discovered catalog pages: {len(result['catalog_urls'])}")
            log(f"Discovered product pages: {len(result['product_urls'])}")
            if req.dry_run:
                log("Dry-run enabled. Skipping database writes.")
                run["counts"]["parsed"] += len(result["items"])
                continue
            counts = upsert_items(result["items"])
            for k, v in counts.items():
                run["counts"][k] += v
            run["counts"]["parsed"] += len(result["items"])
            log(f"Parsed products: {len(result['items'])}")
            log(
                "DB changes: "
                f"added={counts['added']} updated={counts['updated']} unchanged={counts['unchanged']}"
            )
        except Exception as exc:
            run["counts"]["errors"] += 1
            log(f"Source {src.id} failed: {exc}")

    run["status"] = "completed"
    run["finished_at"] = utc_now()
    persist_run(job_id, run)
    write_fallback()


@app.on_event("startup")
def startup() -> None:
    init_db()
    write_fallback()


@app.get("/api/catalog")
def get_catalog() -> dict[str, Any]:
    return read_catalog()


@app.post("/api/catalog/update")
def post_update(req: UpdateRequest) -> dict[str, str]:
    job_id = str(uuid.uuid4())
    run = {
        "status": "running",
        "step_logs": [],
        "started_at": utc_now(),
        "finished_at": None,
        "counts": {"discovered": 0, "parsed": 0, "added": 0, "updated": 0, "unchanged": 0, "errors": 0},
    }
    RUNS[job_id] = run
    persist_run(job_id, run)
    thread = threading.Thread(target=run_update, args=(job_id, req), daemon=True)
    thread.start()
    return {"job_id": job_id}


@app.get("/api/catalog/update/{job_id}")
def get_update(job_id: str) -> dict[str, Any]:
    run = RUNS.get(job_id)
    if run is None:
        with get_conn() as conn:
            row = conn.execute("SELECT * FROM runs WHERE job_id=?", (job_id,)).fetchone()
            if not row:
                return {"status": "not_found", "step_logs": [], "counts": {}}
            return {
                "status": row["status"],
                "step_logs": json.loads(row["logs_json"]),
                "started_at": row["started_at"],
                "finished_at": row["finished_at"],
                "counts": json.loads(row["counts_json"]),
            }
    return run


@app.get("/api/catalog/sources")
def get_sources() -> dict[str, Any]:
    latest_run = None
    with get_conn() as conn:
        row = conn.execute("SELECT * FROM runs ORDER BY started_at DESC LIMIT 1").fetchone()
        if row:
            latest_run = {
                "job_id": row["job_id"],
                "status": row["status"],
                "started_at": row["started_at"],
                "finished_at": row["finished_at"],
                "counts": json.loads(row["counts_json"]),
            }
    return {"sources": [s.__dict__ for s in source_registry()], "latest_run": latest_run}


class ManualImportPayload(BaseModel):
    items: list[dict[str, Any]]


@app.post("/api/catalog/manual-import")
def manual_import(payload: ManualImportPayload) -> dict[str, int]:
    counts = upsert_items(payload.items)
    return {"added": counts["added"]}


def upsert_items(items: list[dict[str, Any]]) -> dict[str, int]:
    counts = {"added": 0, "updated": 0, "unchanged": 0}
    with get_conn() as conn:
        for item in items:
            now = utc_now()
            existing = conn.execute(
                "SELECT id FROM hybrids WHERE name=? AND market=? AND source_url=?",
                (item["name"], item["market"], item["source_url"]),
            ).fetchone()
            had_existing = existing is not None

            cur = conn.execute(
                """INSERT OR IGNORE INTO hybrids(crop, name, brand, market, source_url, last_seen, last_updated)
                   VALUES(?,?,?,?,?,?,?)""",
                (
                    item["crop"],
                    item["name"],
                    item.get("brand"),
                    item["market"],
                    item["source_url"],
                    now,
                    now,
                ),
            )
            if cur.rowcount:
                counts["added"] += 1
            hybrid_id = conn.execute(
                "SELECT id FROM hybrids WHERE name=? AND market=? AND source_url=?",
                (item["name"], item["market"], item["source_url"]),
            ).fetchone()[0]

            attrs = item.get("attributes", [])
            fingerprint = json.dumps(
                sorted((a.get("key"), str(a.get("value")), a.get("evidence", "")) for a in attrs),
                ensure_ascii=False,
            )
            new_hash = hashlib.sha256(fingerprint.encode("utf-8")).hexdigest()
            existing_rows = conn.execute(
                "SELECT key, value, evidence FROM attributes WHERE hybrid_id=?",
                (hybrid_id,),
            ).fetchall()
            existing_fingerprint = json.dumps(
                sorted((r["key"], str(r["value"]), r["evidence"] or "") for r in existing_rows),
                ensure_ascii=False,
            )
            existing_hash = hashlib.sha256(existing_fingerprint.encode("utf-8")).hexdigest()

            if had_existing and new_hash == existing_hash:
                counts["unchanged"] += 1
                conn.execute("UPDATE hybrids SET last_seen=? WHERE id=?", (now, hybrid_id))
                continue

            if had_existing:
                counts["updated"] += 1
            conn.execute("UPDATE hybrids SET last_seen=?, last_updated=? WHERE id=?", (now, now, hybrid_id))
            conn.execute("DELETE FROM attributes WHERE hybrid_id=?", (hybrid_id,))
            for attr in item.get("attributes", []):
                evidence = attr.get("evidence", "")
                conn.execute(
                    """INSERT INTO attributes(hybrid_id, key, value, evidence, evidence_hash, selector, source_url, extracted_at)
                       VALUES(?,?,?,?,?,?,?,?)""",
                    (
                        hybrid_id,
                        attr["key"],
                        attr.get("value"),
                        evidence,
                        hashlib.sha256(evidence.encode("utf-8")).hexdigest() if evidence else None,
                        attr.get("selector"),
                        attr.get("source_url", item["source_url"]),
                        attr.get("extracted_at", now),
                    ),
                )
    write_fallback()
    return counts
