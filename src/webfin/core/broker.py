from . import  Option
from webfin.fin import bsm
from . import OptionResponse
#S0, K, T, r, C0, sigma_est
eval_functions =  {
    'Premium': (lambda opt : bsm.call_premium(opt)),
    'Volatility': (lambda opt : bsm.call_imp_vol(opt.spot,
                                                 opt.strike,
                                                 opt.tenor,
                                                 opt.rate,
                                                 opt.premium,
                                                 opt.volatility))
}


def evaluate(option:Option)->OptionResponse:
    result:float =  eval_functions[option.solveFor](option)
    return OptionResponse(request=option, result= { option.solveFor : str(result)})