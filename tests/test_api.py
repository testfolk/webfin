import json
import pytest

from webfin.cli import init_app


@pytest.fixture
async def client(aiohttp_client):
    app = await init_app()
    return await aiohttp_client(app)


async def test_liveness(client):
    resp = await client.get("/api/v1/healthz")
    assert resp.status == 200, await resp.text()
    data = await resp.text()
    assert data == 'live'


async def test_call_value(client):
    data = {"S0": 100, "K": 105, "T": 1, "r": 0.05, "sigma": 0.2}
    resp = await client.post("/api/v1/bsm/value", json=data)
    assert resp.status == 200, await resp.json()
    data = await resp.json()
    assert data == {'value': 8.021352235143176}
