

from aiohttp import web
from aiohttp_jinja2 import template
from ..fin import BsmCalculator

from . import forms
from ..core  import CalculationRequest



@template('eval.html')
async def optcalc(request):
    optForm = CalculationRequest.CalculationRequest(tenor=0.6, spot=1.3, strike=1.39 ,riskFreeRate=0.0533, volatility=0.3938 )
    form = forms.EvalForm(obj=optForm)
    return {'form': form}


@template('result.html')
async def calculate(request):
    data = await request.post()
    calc = BsmCalculator.BsmCalculator()
    response =  calc.calculate(CalculationRequest.from_request(data))
    return {'spot': data['spot'],'strike': data['strike'], 'tenor': data['tenor'],'premium': response.premium,}


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
