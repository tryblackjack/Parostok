from fastapi.testclient import TestClient

from backend.main import app


def test_catalog_endpoints():
    client = TestClient(app)
    catalog = client.get('/api/catalog')
    assert catalog.status_code == 200
    assert 'crops' in catalog.json()

    update = client.post('/api/catalog/update', json={'markets': ['UA'], 'sources': ['bayer_ua_dekalb']})
    assert update.status_code == 200
    job_id = update.json()['job_id']

    status = client.get(f'/api/catalog/update/{job_id}')
    assert status.status_code == 200
    assert 'status' in status.json()

    sources = client.get('/api/catalog/sources')
    assert sources.status_code == 200
    assert 'sources' in sources.json()
