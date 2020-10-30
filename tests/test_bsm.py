import pytest

from webfin.fin import bsm


def test_call_value():
    given = {"S0": 100, "K": 105, "T": 1, "r": 0.05, "sigma": 0.2}
    expected = pytest.approx(8.020, 8.022)
    actual = bsm.call_value(**given)
    assert actual == expected
