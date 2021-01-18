from aiohttp import web

from webfin.fin import bsm
from webfin.core import Option


async def value(request):
    data = await request.json()
    option = Option(**data)
    v = bsm.call_value(option.spot, option.strike, option.tenor, option.rate, option.volatility)
    return web.json_response({'value': v})


async def vega(request):
    data = await request.json()
    option = Option(**data)
    v = bsm.vega(option.spot, option.strike, option.tenor, option.rate, option.volatility)
    return web.json_response({'value': v})


async def healthz(request):
    return web.Response(text="live")
