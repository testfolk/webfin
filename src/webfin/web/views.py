

from aiohttp import web
from aiohttp_jinja2 import template
from ..fin import BsmCalculator

from . import forms
from ..core  import CalculationRequest
from from_dict import from_dict


@template('eval.html')
async def optcalc(request):

    optForm = CalculationRequest.CalculationRequest(tenor='1y', spot=1.3, strike=1.39, premium=None, riskFreeRate=0.0533, volatility=0.3938, callPut='Call')
    form = forms.EvalForm(obj=optForm)
    return {'form': form}


async def calculate(request):
    data = await request.post()
    req = from_dict(CalculationRequest.CalculationRequest,data)
    calc = BsmCalculator.BsmCalculator()
    response =  calc.calculate( CalculationRequest.CalculationRequest(req))
    return web.Response(text="calculated {}".format(response.premium))

async def value(request):
    data = await request.json()
    S0 = data.get('S0')
    K = data.get('K')
    T = data.get('T')
    r = data.get('r')
    sigma = data.get('sigma')
    v = bsm.call_value(S0, K, T, r, sigma)

    return web.json_response({'value': v})


async def vega(request):
    data = await request.json()
    S0 = data.get('S0')
    K = data.get('K')
    T = data.get('T')
    r = data.get('r')
    sigma = data.get('sigma')
    v = bsm.vega(S0, K, T, r, sigma)
    return web.json_response({'value': v})


async def healthz(request):
    return web.Response(text="live")
