import { useEffect, useMemo, useState } from 'react';

const API = 'http://localhost:8000';

export default function App() {
  const [catalog, setCatalog] = useState({ crops: {} });
  const [sources, setSources] = useState({ sources: [], latest_run: null });
  const [job, setJob] = useState(null);
  const [logs, setLogs] = useState([]);
  const [offline, setOffline] = useState(false);
  const [selected, setSelected] = useState(null);

  const varieties = useMemo(() => Object.values(catalog.crops).flat(), [catalog]);

  useEffect(() => {
    loadAll();
  }, []);

  async function loadAll() {
    try {
      const [catalogRes, sourceRes] = await Promise.all([
        fetch(`${API}/api/catalog`),
        fetch(`${API}/api/catalog/sources`),
      ]);
      setCatalog(await catalogRes.json());
      setSources(await sourceRes.json());
      setOffline(false);
    } catch {
      const fallback = await fetch('/catalog_fallback.json');
      setCatalog(await fallback.json());
      setOffline(true);
    }
  }

  async function updateCatalog() {
    const res = await fetch(`${API}/api/catalog/update`, {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ markets: ['UA', 'US'], sources: ['bayer_ua_dekalb', 'bayer_us_dekalb'] }),
    });
    const { job_id } = await res.json();
    setJob(job_id);
    const interval = setInterval(async () => {
      const statusRes = await fetch(`${API}/api/catalog/update/${job_id}`);
      const status = await statusRes.json();
      setLogs(status.step_logs || []);
      if (status.status !== 'running') {
        clearInterval(interval);
        await loadAll();
      }
    }, 600);
  }

  return (
    <main style={{ fontFamily: 'Arial', margin: 24 }}>
      <h1>AgroSim Parostok</h1>
      <p><strong>MODELING ONLY:</strong> Simulation outputs are synthetic and not measured biological results.</p>
      {offline && <p style={{ color: '#9a6700' }}>Offline catalog snapshot</p>}
      <button onClick={updateCatalog}>Update Hybrid Database</button>
      {job && <p>Job: {job}</p>}
      <pre style={{ background: '#111', color: '#7CFC00', padding: 12, minHeight: 70 }}>{logs.map((l) => `> ${l.message}`).join('\n')}</pre>

      <h2>Varieties</h2>
      <ul>
        {varieties.map((v) => (
          <li key={`${v.id}-${v.name}`}>
            <button onClick={() => setSelected(v)}>{v.name} ({v.market})</button>{' '}
            <a href={v.source_url} target="_blank">source</a>
          </li>
        ))}
      </ul>

      {selected && (
        <section>
          <h3>Info / Provenance: {selected.name}</h3>
          <ul>
            {selected.attributes.map((a, idx) => (
              <li key={idx}>{a.key}: {String(a.value ?? 'unknown')} | {a.evidence || 'no snippet'} | {a.extracted_at}</li>
            ))}
          </ul>
        </section>
      )}

      <h2>Data Integrity Report</h2>
      <p>Enabled sources: {sources.sources.filter((s) => s.enabled).length} / {sources.sources.length}</p>
      <ul>
        {sources.sources.map((s) => (
          <li key={s.id}>{s.id} ({s.market}) - {s.enabled ? 'enabled' : `disabled: ${s.reason}`}</li>
        ))}
      </ul>
      {sources.latest_run && <p>Last update status: {sources.latest_run.status}</p>}
      <p>Deterministic variety seed is used only for demo repeatability (synthetic variability).</p>
    </main>
  );
}
