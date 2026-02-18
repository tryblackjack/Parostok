from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup


@dataclass
class BayerUADekalbScraper:
    market: str = "UA"
    start_url: str = "https://www.cropscience.bayer.ua/Products/Dekalb"
    brand: str = "DEKALB (Bayer)"

    def fetch(self, url: str) -> str:
        req = Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (compatible; ParostokBot/1.0)",
                "Accept-Language": "uk-UA,uk;q=0.9,en;q=0.8",
            },
        )
        with urlopen(req, timeout=30) as resp:
            return resp.read().decode("utf-8", errors="ignore")

    @staticmethod
    def _clean(s: str) -> str:
        return re.sub(r"\s+", " ", s).strip()

    def _find_first(self, pattern: str, text: str) -> str | None:
        m = re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE)
        return m.group(1).strip() if m else None

    def _find_block(self, after_heading: str, text: str) -> str | None:
        h = re.escape(after_heading)
        m = re.search(rf"{h}\s+(.*?)(?=\n[A-ZА-ЯІЇЄҐ0-9 \-]{{5,}}\n|\Z)", text, flags=re.DOTALL)
        return self._clean(m.group(1)) if m else None

    def _parse_kv_lines(self, block: str) -> dict[str, str]:
        out: dict[str, str] = {}
        if not block:
            return out
        for line in block.split("\n"):
            line = self._clean(line)
            if ":" not in line:
                continue
            k, v = line.split(":", 1)
            k = self._clean(k)
            v = self._clean(v)
            if k and v:
                out[k] = v
        return out

    def _parse_ratings(self, block: str) -> dict[str, int]:
        ratings: dict[str, int] = {}
        if not block:
            return ratings
        for line in block.split("\n"):
            line = self._clean(line)
            m = re.match(r"^(.*?)(\d{1,2})$", line)
            if not m:
                continue
            label = self._clean(re.sub(r"[●○•\.\-]+", " ", m.group(1)))
            score = int(m.group(2))
            if label:
                ratings[label] = score
        return ratings

    def discover_catalog_pages(self) -> list[str]:
        html = self.fetch(self.start_url)
        soup = BeautifulSoup(html, "html.parser")
        found: set[str] = set()
        for a in soup.select("a[href]"):
            href = a.get("href", "")
            full = urljoin(self.start_url, href)
            parsed = urlparse(full)
            if parsed.netloc != "www.cropscience.bayer.ua":
                continue
            if "/Products/Dekalb/" not in parsed.path:
                continue
            if parsed.path.rstrip("/") == "/Products/Dekalb":
                continue
            if parsed.path.count("/") == 3:
                found.add(full.split("?")[0])
        return sorted(found)

    def discover_product_pages(self, catalog_url: str) -> list[str]:
        html = self.fetch(catalog_url)
        soup = BeautifulSoup(html, "html.parser")
        found: set[str] = set()
        path_prefix = urlparse(catalog_url).path.rstrip("/") + "/"
        for a in soup.select("a[href]"):
            href = a.get("href", "")
            full = urljoin(catalog_url, href).split("?")[0]
            parsed = urlparse(full)
            if parsed.netloc != "www.cropscience.bayer.ua":
                continue
            if not parsed.path.startswith(path_prefix):
                continue
            if parsed.path.rstrip("/") == path_prefix.rstrip("/"):
                continue
            if parsed.path.count("/") >= 4:
                found.add(full)
        return sorted(found)

    def parse_product(self, product_url: str) -> dict[str, Any]:
        html = self.fetch(product_url)
        soup = BeautifulSoup(html, "html.parser")

        h1 = soup.find("h1")
        name = self._clean(h1.get_text(" ", strip=True)) if h1 else None

        text = soup.get_text("\n", strip=True).replace("\u00a0", " ")
        text = re.sub(r"\n{2,}", "\n", text).strip()

        fao = self._find_first(r"ФАО:\s*([0-9]{2,4})", text)
        grain_type = self._find_first(r"Тип зерна:\s*([^\n]+)", text)
        maturity = self._find_first(r"Група стиглості:\s*([^\n]+)", text)

        advantages = self._find_block("ОСНОВНІ ПЕРЕВАГИ", text)
        positioning = self._find_block("ПОЗИЦІОНУВАННЯ ГІБРИДА", text)
        density = self._find_block("ГУСТОТА НА ЧАС ЗБИРАННЯ", text)
        characteristics = self._find_block("ХАРАКТЕРИСТИКА ГІБРИДА", text)

        positioning_kv = self._parse_kv_lines(positioning) if positioning else {}
        density_kv = self._parse_kv_lines(density) if density else {}
        ratings = self._parse_ratings(characteristics) if characteristics else {}

        crop = None
        try:
            crop = product_url.split("/Products/Dekalb/")[1].split("/")[0].lower()
        except Exception:
            crop = None

        item: dict[str, Any] = {
            "market": self.market,
            "brand": self.brand,
            "name": name,
            "crop": crop,
            "source_url": product_url,
            "attributes": [],
        }

        def add_attr(key: str, value: Any, evidence: str | None) -> None:
            if value is None or value == "":
                return
            item["attributes"].append(
                {
                    "key": key,
                    "value": value,
                    "selector": "regex_on_page_text",
                    "evidence": (evidence or str(value))[:240],
                    "source_url": product_url,
                }
            )

        add_attr("fao", fao, f"ФАО: {fao}" if fao else None)
        add_attr("grain_type", grain_type, f"Тип зерна: {grain_type}" if grain_type else None)
        add_attr("maturity_group", maturity, f"Група стиглості: {maturity}" if maturity else None)

        if advantages:
            add_attr("advantages_text", advantages, advantages)

        for k, v in positioning_kv.items():
            add_attr(f"positioning.{k}", v, f"{k}: {v}")

        for k, v in density_kv.items():
            add_attr(f"density.{k}", v, f"{k}: {v}")

        for k, score in ratings.items():
            add_attr(f"rating.{k}", score, f"{k} {score}")

        return item

    def run(self) -> dict[str, Any]:
        catalog_urls = self.discover_catalog_pages()
        product_urls: set[str] = set()
        for catalog_url in catalog_urls:
            product_urls.update(self.discover_product_pages(catalog_url))

        items: list[dict[str, Any]] = []
        for product_url in sorted(product_urls):
            item = self.parse_product(product_url)
            if item.get("name"):
                items.append(item)

        return {"catalog_urls": catalog_urls, "product_urls": sorted(product_urls), "items": items}
