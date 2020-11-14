from typing import NamedTuple


class Option(NamedTuple):
    spot: float  # S0
    tenor: float  # T
    strike: float  # K
    rate: float  # r
    volatility: float  # sigma

    @classmethod
    def from_request(cls, data):
        return cls(**data)
