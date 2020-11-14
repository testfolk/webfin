import pytest

from webfin.fin import Option, bsm

option_sample = Option(spot=100, tenor=1, strike=105, rate=0.05, volatility=0.2)

call_premium_cases = [
    pytest.param(option_sample._replace(tenor=0), None, marks=pytest.mark.xfail, id='division-by-zero'),
    pytest.param(option_sample, pytest.approx(8.020, 8.022), marks=pytest.mark.xfail, id='basic-case'),
    pytest.param(option_sample._replace(rate=1.9), pytest.approx(84.20, 84.30), id='high-rate'),
    pytest.param(option_sample._replace(volatility=1), pytest.approx(84.20, 84.30), id='stable-volatility'),
    pytest.param(option_sample._replace(volatility=0), None, marks=pytest.mark.xfail, id='zero-volatility'),
]


def test_call_value():
    given = {"S0": 100, "K": 105, "T": 1, "r": 0.05, "sigma": 0.2}
    expected = pytest.approx(8.020, 8.022)
    actual = bsm.call_value(**given)
    assert actual == expected


@pytest.mark.parametrize('option, premium', call_premium_cases)
def test_call_premium(option, premium):
    actual = bsm.call_premium(option)
    assert actual == premium
