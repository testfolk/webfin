import aiohttp_jinja2
from aiohttp import web

from webfin.fin import Option, bsm

from . import forms


async def optcalc(request):
    if request.method == 'GET':
        option = Option(tenor=0.6, spot=1.3, strike=1.39, rate=0.0533, volatility=0.3938)
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


async def healthz(request):
    return web.Response(text="live")
