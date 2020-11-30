from aiohttp import web

from webfin.fin import bsm, Option


async def premium(request):
    data = await request.json()
    option = Option.from_request(data)
    v = bsm.call_premium(option)
    return web.json_response({'value': v})


async def vega(request):
    data = await request.json()
    option = Option.from_request(data)
    v = bsm.vega(option)
    return web.json_response({'value': v})


async def healthz(request):
    return web.Response(text="live")
