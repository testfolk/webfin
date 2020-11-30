import pytest

from webfin.fin import Option, bsm, broker

option_sample = Option(spot=100, tenor=1, strike=105, rate=0.05, volatility=0.2, premium=0.0, solveFor='Premium')

call_premium_cases = [
    pytest.param(option_sample, pytest.approx(8.020, 8.022), id='basic-case'),
    pytest.param(option_sample._replace(rate=1.9), pytest.approx(84.20, 84.30), id='high-rate'),
    pytest.param(option_sample._replace(tenor=0), None, marks=pytest.mark.xfail, id='division-by-zero'),
    pytest.param(option_sample._replace(volatility=1), pytest.approx(84.20, 84.30), id='stable-volatility'),
    pytest.param(option_sample._replace(volatility=0), None, marks=pytest.mark.xfail, id='zero-volatility'),
]


@pytest.mark.parametrize('option, premium', call_premium_cases)
def test_call_premium(option, premium):
    actual = bsm.call_premium(option)
    assert actual == premium


@pytest.mark.parametrize('option, vega', call_premium_cases)
def test_call_vega(option, vega):
    actual = bsm.vega(option)
    assert actual == vega


def test_call_impl_vol():
    actual = bsm.call_imp_vol(0.9, 1.3, 0.5, 0.09, 0.099, 0.5)
    assert actual == pytest.approx(0.78096471114)


def test_service_broker(mocker):
    # TODO: would be best to move this broker test into it's own file ?
    # TODO: is there a way to directly test that the method has been invoked rather than having to set up
    # a fake answer ?
    impl_Vol_answer = 4.2023
    call_premium_answer = 6.0755

    mocker.patch('webfin.fin.broker.bsm.call_imp_vol', return_value=impl_Vol_answer)
    mocker.patch('webfin.fin.broker.bsm.call_premium', return_value=call_premium_answer)

    assert broker.evaluate(option_sample._replace(solveFor='Premium')) == call_premium_answer
    assert broker.evaluate(option_sample._replace(solveFor='Volatility', premium='0.1')) == impl_Vol_answer

    with pytest.raises(KeyError):
        broker.evaluate(option_sample._replace(solveFor='X', premium='0.1')) == impl_Vol_answer
