from . import Option
from . import bsm

#S0, K, T, r, C0, sigma_est
eval_functions =  {
    'Premium': (lambda opt : bsm.call_premium(opt)),
    'Volatility': (lambda opt : bsm.call_imp_vol(opt.spot,
                                                 opt.strike,
                                                 opt.tenor,
                                                 opt.rate,
                                                 opt.premium,
                                                 opt.volatility)),

}


def evaluate(option:Option)->float:
        return eval_functions[option.solveFor](option)
