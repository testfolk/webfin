import aiohttp_jinja2
from aiohttp import web

from webfin.fin import Option, bsm

from . import forms


async def optcalc(request):
    if request.method == 'GET':
        params = request.rel_url.query
        sf = 'Premium' if 'sf' not in params else params['sf']
        option = Option(tenor=0.5, spot=1.3, strike=1.39, rate=0.0533, volatility=0.3938)
        form = forms.OptionForm(obj=option, premium=0.0, solveFor=sf)
        context = {'form': form, 'sf': sf}
        response = aiohttp_jinja2.render_template('eval.html', request, context)
        return response

    elif request.method == 'POST':
        data = await request.post()
        form = forms.OptionForm(data)
        option = Option.from_request({k: v for k, v in form.data.items() if k in Option._fields})
        sf = form.data['solveFor']
        if sf == 'Premium':
            premium = bsm.call_premium(option)
            form.data['premium'] = premium
            context = {'premium': premium, 'form': form}
        else:
            value = bsm.vega(option)
            form.data['value'] = value
            context = {'value': value, 'form': form}
        response = aiohttp_jinja2.render_template('eval.html', request, context)
        return response


async def healthz(request):
    return web.Response(text="live")


async def index(request):
    params = request.rel_url.query
    sf = 'Premium' if 'sf' not in params else params['sf']
    option = Option(tenor=0.5, spot=1.3, strike=1.39, rate=0.0533, volatility=0.3938)
    form = forms.OptionForm(obj=option, premium=0.0, solveFor=sf)
    context = {'form': form, 'sf': sf}
    response = aiohttp_jinja2.render_template('option.html', request, context)
    return response
