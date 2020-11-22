import pytest

from webfin.cli import init_app
from htmldom import htmldom


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
    page = htmldom.HtmlDom().createDom(txt)

    volField = page.find("#volatility")
    assert volField.first() is not None
    assert page.find("#premium").first() is None


async def test_optcalc_route_with_solve_for_volatility(client):
    resp = await client.get("/optcalc?sf=Volatility")

    txt = await resp.text()
    page = htmldom.HtmlDom().createDom(txt)
    assert page.find("#premium").first() is not None
    assert page.find("#volatility").first() is  None


async def test_optcalc_route_with_solve_for_volatility(client):
    resp = await client.get("/optcalc?sf=Premium")
    txt = await resp.text()
    page = htmldom.HtmlDom().createDom(txt)
    assert page.find("#volatility").first() is not None
    assert page.find("#premium").first() is  None

