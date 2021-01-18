import warnings

warnings.filterwarnings('ignore', category=DeprecationWarning)

import pytest
import test_utils.option_utils as optutil
from webfin.cli import init_app
from lxml import html


@pytest.fixture
async def client(aiohttp_client):
    warnings.filterwarnings('ignore', category=DeprecationWarning)
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
        doc.get_element_by_id('premium')


async def test_optcalc_route_with_solve_for_volatility(client):
    resp = await client.get("/optcalc?sf=Volatility")
    txt = await resp.text()
    doc = html.fromstring(txt)
    vol = doc.get_element_by_id('volatility')
    assert vol.value == '0.3938'
    label = doc.get_element_by_id('opt_calc_volatility_label')
    assert label.text.strip() == 'Est. Vol.'


async def test_optcalc_route_with_solve_for_premium(client):
    resp = await client.get("/optcalc?sf=Premium")
    txt = await resp.text()
    doc = html.fromstring(txt)

    with pytest.raises(KeyError):
        doc.get_element_by_id('premium')


async def test_optcalc_post_with_valid_data_and_calc_ok(client):
    resp = await client.post("/optcalc?sf=Premium", data=optutil.valid_solve_for_premium_data())
    assert (resp.status == 200)
    txt = await resp.text()
    doc = html.fromstring(txt)
    error_elements = doc.find_class('optcalc_error_message')
    assert len(error_elements) == 0
    assert len(doc.find_class('optcalc_result_solution')) == 1
    assert len(doc.find_class('optcalc_result_detail')) == 4


async def test_optcalc_post_with_valid_solve_for_vol_data(client):
    resp = await client.post("/optcalc?sf=Volatility", data=optutil.valid_solve_for_vol_data())
    assert (resp.status == 200)
    txt = await resp.text()
    doc = html.fromstring(txt)
    error_els = doc.find_class('optcalc_error_message')
    assert len(error_els) == 0
    assert len(doc.find_class('optcalc_result_solution')) == 1
    assert len(doc.find_class('optcalc_result_detail')) == 4
    assert len(client.app['results_store']) == 1


async def test_optcalc_solve_for_vol_with_zero_premium(client):
    resp = await client.post("/optcalc?sf=Volatility", data=optutil.solve_for_vol_with_zero_premium())
    assert (resp.status == 200)
    txt = await resp.text()
    doc = html.fromstring(txt)
    error_els = doc.find_class('alert-danger')
    assert len(client.app['results_store']) == 0
    assert len(error_els) == 1
    assert len(doc.find_class('optcalc_result_solution')) == 0
    assert len(doc.find_class('optcalc_result_detail')) == 0
