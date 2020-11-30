import traceback

import aiohttp_jinja2
from aiohttp import web


async def handle_404(request, error):
    return aiohttp_jinja2.render_template('404.html', request, {}, status=404)


async def handle_500(request, error):
    if request.rel_url.path.startswith('/api'):
        return web.json_response({'error': str(error)}, status=500)
    return aiohttp_jinja2.render_template('500.html', request, {}, status=500)


def create_error_middleware(overrides):
    @web.middleware
    async def error_middleware(request, handler):
        try:
            return await handler(request)
        except web.HTTPException as ex:
            print(traceback.format_exc())
            override = overrides.get(ex.status)
            if override:
                return await override(request, ex)
            raise
        except Exception as e:
            print(traceback.format_exc())
            return await overrides[500](request, e)

    return error_middleware


def setup_middlewares(app):
    error_middleware = create_error_middleware({
        404: handle_404,
        500: handle_500
    })
    app.middlewares.append(error_middleware)
