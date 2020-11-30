from typing import NamedTuple


class Option(NamedTuple):
    spot: float  # S0
    tenor: float  # T
    strike: float  # K
    rate: float  # r
    volatility: float  # sigma

    @classmethod
    def from_request(cls, data):
        data = {k: float(v) for k, v in data.items()}
        return cls(**data)
