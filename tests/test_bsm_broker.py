import pytest
from webfin.core import broker
from webfin.core import Option
from webfin.core import OptionResponse
from webfin.core import ResultItem

option_sample = Option(spot=100, tenor=1, strike=105, rate=0.05, volatility=0.2, premium=0.0, solveFor='Premium')

impl_Vol_answer = 0.556686

call_premium_answer = 0.9033944


def mock_the_service(mocker):
    mocker.patch('webfin.fin.broker.bsm.call_imp_vol', return_value=impl_Vol_answer)
    mocker.patch('webfin.fin.broker.bsm.call_value', return_value=call_premium_answer)


def test_solve_for_premium_routing(mocker):
    mock_the_service(mocker)
    actual_result: OptionResponse = broker.evaluate(option_sample._replace(solveFor='Premium'))
    assert actual_result.request.solveFor == 'Premium'
    assert actual_result.solution.content == str(call_premium_answer)
    assert actual_result.details[0].caption == 'Spot'
    assert actual_result.details[1].caption == 'Strike'
    assert actual_result.details[2].caption == 'Risk free rate'
    assert actual_result.details[3].caption == 'Tenor'

    assert actual_result.details[0].content == str(actual_result.request.spot)
    assert actual_result.details[1].content == str(actual_result.request.strike)
    assert actual_result.details[2].content == str(actual_result.request.rate)
    assert actual_result.details[3].content == str(actual_result.request.tenor)


def test_solve_for_impl_vol_routing(mocker):
    mock_the_service(mocker)
    actual_result: OptionResponse = broker.evaluate(option_sample._replace(solveFor='Volatility'))
    assert actual_result.request.solveFor == 'Volatility'
    assert actual_result.solution.content == str(impl_Vol_answer)
    assert actual_result.solution.caption == 'Impl. Vol.'


def test_service_broker_fails_with_invalid_solve_for(mocker):
    # TODO: is there a way to directly test that the method has been invoked rather than having to set up
    # a fake answer ?

    # TODO is there a way to put this mock into a setup method or a fixture ?
    mock_the_service(mocker)

    with pytest.raises(KeyError):
        broker.evaluate(option_sample._replace(solveFor='X', premium='0.1')) == impl_Vol_answer
