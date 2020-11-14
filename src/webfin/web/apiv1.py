from aiohttp import web

from webfin.fin import bsm, Option


async def value(request):
    data = await request.json()
    option = Option(**data)
    v = bsm.call_premium(option)
    return web.json_response({'value': v})


async def vega(request):
    data = await request.json()
    option = Option(**data)
    v = bsm.vega(option)
    return web.json_response({'value': v})


async def healthz(request):
    return web.Response(text="live")
