from collections import namedtuple
import pytest
from unittest import mock
from webfin.core import broker
from webfin.core import Option
from webfin.core import OptionResponse
from webfin.core import ResultItem

option_sample = Option(spot=100, tenor=1, strike=105, rate=0.05, volatility=0.2, premium=0.0, solveFor='Premium')

nt = namedtuple('Answer', 'vol premium')
answers = (
    # vol, premium
    nt(0.556686, 8.02135),
)


@pytest.fixture(params=answers)
def answer(request):
    return request.param


@pytest.fixture(autouse=True)
def mock_the_service(request, answer):
    """This will apply to all tests in this module"""
    patch_imp_vol = mock.patch('webfin.core.broker.bsm.call_imp_vol',
                               return_value=answer.vol)
    patch_premium = mock.patch('webfin.core.broker.bsm.call_value',
                               return_value=answer.premium)

    def teardown():
        patch_imp_vol.start()
        patch_premium.start()

    request.addfinalizer(teardown)


def test_solve_for_premium_routing(answer):
    actual = broker.evaluate(option_sample._replace(solveFor='Premium'))
    expected = OptionResponse(
        request=Option(spot=100,
                       tenor=1,
                       strike=105,
                       rate=0.05,
                       volatility=0.2,
                       premium=0.0,
                       solveFor='Premium'),
        solution=ResultItem(caption='Premium',
                            content=pytest.approx(answer.premium)),
        details=[ResultItem(caption='Spot', content='100'),
                 ResultItem(caption='Strike', content='105'),
                 ResultItem(caption='Risk free rate', content='0.05'),
                 ResultItem(caption='Tenor', content='1')])

    assert actual == expected


def test_solve_for_impl_vol_routing(answer):
    actual = broker.evaluate(option_sample._replace(solveFor='Volatility'))
    expected = OptionResponse(
        request=Option(spot=100,
                       tenor=1,
                       strike=105,
                       rate=0.05,
                       volatility=0.2,
                       premium=0.0,
                       solveFor='Volatility'),
        solution=ResultItem(caption='Impl. Vol.', content=pytest.approx(0.556686)),
        details=[ResultItem(caption='Spot', content='100'),
                 ResultItem(caption='Strike', content='105'),
                 ResultItem(caption='Risk free rate', content='0.05'),
                 ResultItem(caption='Tenor', content='1')])
    assert actual == expected


def test_service_broker_fails_with_invalid_solve_for(answer):
    # TODO: is there a way to directly test that the method has been invoked rather than having to set up
    # a fake answer ?
    with pytest.raises(KeyError):
        pass
        # broker.evaluate(option_sample._replace(solveFor='X', premium='0.1')) == answer.vol
