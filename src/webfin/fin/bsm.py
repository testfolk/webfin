"""
Examples taken from the book Python for Finance
Python for Finance by Yves Hilpisch (O’Reilly). Copyright 2015 Yves Hilpisch, 978-1-491-94528-5.
Analytical Black-Scholes-Merton (BSM) Formula
"""
import logging
from math import exp, log, sqrt

from scipy import stats

from . import Option

logger = logging.getLogger(__name__)


def call_premium(option: Option) -> float:
    S0 = option.spot
    K = option.strike
    T = option.tenor
    r = option.rate
    sigma = option.volatility
    d1 = (log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * sqrt(T))
    d2 = (log(S0 / K) + (r - 0.5 * sigma**2) * T) / (sigma * sqrt(T))
    premium = (S0 * stats.norm.cdf(d1, 0.0, 1.0) - K * exp(-r * T) * stats.norm.cdf(d2, 0.0, 1.0))
    # stats.norm.cdf —> cumulative distribution function for normal distribution
    return premium


def vega(option: Option):
    """Vega of European option in BSM model"""
    S0 = option.spot
    K = option.strike
    T = option.tenor
    r = option.rate
    sigma = option.volatility
    d1 = (log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * sqrt(T))
    v = S0 * stats.norm.cdf(d1, 0.0, 1.0) * sqrt(T)
    return v


def call_imp_vol(S0, K, T, r, C0, sigma_est, it=100):
    """Implied volatility of European call option in BSM model.
        Parameters
        ==========
        S0 : float
            initial stock/index level
        K : float
            strike price
        T : float
            maturity date (in year fractions)
        r : float constant risk-free short rate
        sigma_est : float estimate of impl. volatility
        it : integer number of iterations
    Returns
    =======
    simga_est : float
            numerically estimated implied volatility
    """

    for _ in range(it):
        sigma_est -= ((call_premium(Option(strike= K, tenor=T, rate=r, volatility=sigma_est,spot=S0,premium=C0)) - C0) / vega(Option(strike=K, tenor=T, rate=r, volatility=sigma_est,premium=C0,spot=S0)))
    return sigma_est
