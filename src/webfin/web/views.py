import aiohttp_jinja2
from aiohttp import web
from webfin.fin import Option, bsm

from . import forms


async def optcalc(request):
    if request.method == 'GET':
        option = Option( tenor=0.6, spot=1.3, strike=1.39, rate=0.0533, volatility=0.3938)
        form = forms.OptionForm(obj=option)
        context = {'form': form}
        response = aiohttp_jinja2.render_template('eval.html', request, context)
        return response
    elif request.method == 'POST':
        data = await request.post()
        form = forms.OptionForm(data)
        option = Option.from_request(form.data)
        premium = bsm.call_premium(option)
        context = {'premium': premium, 'form': form}
        response = aiohttp_jinja2.render_template('eval.html', request, context)
        return response


async def calculate(request):
    data = await request.post()
    f = forms.OptionForm(data)
    option = Option.from_request(f.data)
    premium = bsm.call_premium(option)
    context = {'premium': premium, **data}
    response = aiohttp_jinja2.render_template('result.html', request, context)
    return response


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
