import abc
from ..fin import BsmCalculator
from ..core import CalculationRequest
from ..core import CalculationResponse
class Calculator(abc.ABC):
    @abc.abstractmethod
    def calculate(self,request:CalculationRequest.CalculationRequest )->CalculationResponse.CalculationResponse:
        pass



