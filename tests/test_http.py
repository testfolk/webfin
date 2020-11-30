import pytest

from webfin.cli import init_app
from lxml import html


@pytest.fixture
async def client(aiohttp_client):
    app = await init_app()
    return await aiohttp_client(app)


async def test_optcalc_route(client):
    resp = await client.get("/optcalc")
    assert resp.status == 200


async def test_optcalc_route_with_default_solve_for(client):
    resp = await client.get("/optcalc")
    txt = await resp.text()
    doc = html.fromstring(txt)
    with pytest.raises(KeyError):
        doc.get_element_by_id('volatility')
    premium = doc.get_element_by_id('premium')
    assert premium.value == '0.0'


async def test_optcalc_route_with_solve_for_volatility(client):
    resp = await client.get("/optcalc?sf=Volatility")
    txt = await resp.text()
    doc = html.fromstring(txt)
    vol = doc.get_element_by_id('volatility')
    assert vol.value == '0.3938'


async def test_optcalc_route_with_solve_for_volatility(client):
    resp = await client.get("/optcalc?sf=Premium")
    txt = await resp.text()
    doc = html.fromstring(txt)
    premium = doc.get_element_by_id('premium')
    assert premium.value == '0.0'
