from ..core import Calculator
from ..core import CalculationRequest
from ..core import  CalculationResponse
from . import bsm

class BsmCalculator(Calculator.Calculator):
    def __init__(self):
        super().__init__()

    def calculate(self,request:CalculationRequest.CalculationRequest )->CalculationResponse.CalculationResponse:
        # S0, K, T, r, sigma
        premium = bsm.call_value(request.spot,request.strike,0.5,request.riskFreeRate,request.volatility)
        return CalculationResponse.CalculationResponse(premium=premium)
