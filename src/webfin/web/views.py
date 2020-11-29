import aiohttp_jinja2
from aiohttp import web


from webfin.fin import bsm
from webfin.core import Option
from webfin.core import OptionResponse
from webfin.core import broker

from . import forms



async def optcalc(request):
    if request.method == 'GET':
        params = request.rel_url.query
        sf = 'Premium' if 'sf' not in params else params['sf']
        option = Option(tenor=0.5, spot=1.3, strike=1.39, rate=0.0533, volatility=0.3938, premium=0.0, solveFor=sf)
        form = forms.OptionForm(obj=option)
        context = {'form': form, 'sf': sf, 'result': None}
        response = aiohttp_jinja2.render_template('eval.html', request, context)
        return response

    elif request.method == 'POST':
        data = await request.post()
        form = forms.OptionForm(data)
        option:Option = Option.from_request(form.data)
        response:OptionResponse = broker.evaluate(option)
        context = {'form': form, 'result' : response}
        response = aiohttp_jinja2.render_template('eval.html', request, context)
        return response


async def healthz(request):
    return web.Response(text="live")
