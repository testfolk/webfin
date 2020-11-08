import dataclasses
@dataclasses.dataclass
class CalculationRequest:
    tenor:float
    spot: float
    strike: float
    riskFreeRate: float
    volatility: float

def from_request( data):
    return CalculationRequest(
        tenor = float(data['tenor']),
        spot = float(data['spot']),
        strike = float(data['strike']),
        riskFreeRate = float(data['riskFreeRate']),
        volatility=float(data['volatility']))