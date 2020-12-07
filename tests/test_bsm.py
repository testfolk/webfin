import pytest

from webfin.fin import bsm
from webfin.core import Option

option_sample = Option(spot=100, tenor=1, strike=105, rate=0.05, volatility=0.2, premium=0.0)

call_premium_cases = [
    pytest.param(option_sample, pytest.approx(8.020, 8.022), id='basic-case'),
    pytest.param(option_sample._replace(rate=1.9), pytest.approx(84.20, 84.30), id='high-rate'),
    pytest.param(option_sample._replace(tenor=0), None, marks=pytest.mark.xfail, id='division-by-zero'),
    pytest.param(option_sample._replace(volatility=1), pytest.approx(84.20, 84.30), id='stable-volatility'),
    pytest.param(option_sample._replace(volatility=0), None, marks=pytest.mark.xfail, id='zero-volatility'),
]


@pytest.mark.parametrize('option, premium', call_premium_cases)
def test_call_premium(option: Option, premium):
    actual = bsm.call_value(option.spot, option.strike, option.tenor, option.rate, option.volatility)
    assert actual == premium


@pytest.mark.parametrize('option, vega', call_premium_cases)
def test_call_vega(option, vega):
    actual = bsm.vega(option.spot, option.strike, option.tenor, option.rate, option.volatility)
    assert actual == vega
