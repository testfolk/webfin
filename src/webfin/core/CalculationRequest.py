import dataclasses

@dataclasses.dataclass
class CalculationRequest:
    tenor:str
    spot: float
    strike: float
    premium: float
    riskFreeRate: float
    volatility: float
    callPut: str


