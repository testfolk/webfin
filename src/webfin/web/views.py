from aiohttp import web
from webfin.fin import bsm


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
