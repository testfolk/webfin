import dataclasses

@dataclasses.dataclass
class CalculationResponse:
    premium: float
    volatility: float
    solvedFor: str




