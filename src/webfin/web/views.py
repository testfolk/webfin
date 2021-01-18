import aiohttp_jinja2
from aiohttp import web
from webfin.core import Option
from webfin.core import OptionResponse
from webfin.core import broker
from . import forms


async def optcalc(request):
    results_store = request.app['results_store']
    if request.method == 'GET':
        results_store.clear()
        params = request.rel_url.query
        sf = 'Premium' if 'sf' not in params else params['sf']
        option = Option(tenor=0.5, spot=1.3, strike=1.39, rate=0.0533, volatility=0.3938, premium=0.0, solveFor=sf)
        form = forms.OptionForm(obj=option)
        context = {'form': form, 'sf': sf, 'results': results_store}
        response = aiohttp_jinja2.render_template('eval.html', request, context)
        return response

    elif request.method == 'POST':
        data = await request.post()
        form = forms.OptionForm(data)
        result: OptionResponse = None
        if form.validateSolveFor() is True:
            option: Option = Option.from_request(form.data)
            result = broker.evaluate(option)
            results_store.append(result)

        context = {'form': form, 'results': results_store, 'sf': form.solveFor.data}

        resp = aiohttp_jinja2.render_template('eval.html', request, context)
        return resp


async def healthz(request):
    return web.Response(text="live")
