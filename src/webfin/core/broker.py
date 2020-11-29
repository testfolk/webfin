from . import  Option
from webfin.fin import bsm
from . import OptionResponse
from . import ResultItem
from typing import List
#S0, K, T, r, C0, sigma_est


def solveForPremium(opt:Option)->OptionResponse:

    decimalResult:float = bsm.call_value(opt.spot,opt.strike,opt.tenor,opt.rate,opt.volatility)
    solution:ResultItem = ResultItem(caption="Premium",content=str(decimalResult))
    details: List[ResultItem] = [
        ResultItem(caption="Spot", content=str(opt.spot)),
        ResultItem(caption="Strike", content=str(opt.strike)),
        ResultItem(caption="Risk free rate", content=str(opt.rate)),
        ResultItem(caption="Tenor", content=str(opt.tenor))
    ]

    return OptionResponse(request=opt,solution=solution, details=details)


def solveForImplVol(opt:Option)->OptionResponse:

    decimalResult =  bsm.call_imp_vol(opt.spot,opt.strike,opt.tenor,opt.rate,opt.premium,opt.volatility)

    solution: ResultItem =  ResultItem(caption="Impl. Vol." , content=str(decimalResult))
    details:List[ResultItem] = [
        ResultItem(caption="Spot",content=str(opt.spot)),
        ResultItem(caption="Strike", content=str(opt.strike)),
        ResultItem(caption="Risk free rate", content=str(opt.rate)),
        ResultItem(caption="Tenor", content=str(opt.tenor))
    ]
    return OptionResponse(request=opt,solution = solution,details= details)


eval_functions =  {
    'Premium': solveForPremium,
    'Volatility': solveForImplVol
}




def evaluate(option:Option)->OptionResponse:
    return   eval_functions[option.solveFor](option)
