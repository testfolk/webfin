import webfin

from . import views


def setup_routes(app, prefix=''):
    # app.router.add_get(f'{prefix}/', index)
    app.router.add_post(f'{prefix}/bsm/value', views.value, name='value')
    app.router.add_post(f'{prefix}/bsm/vega', views.vega, name='vega')
    app.router.add_get(f'{prefix}/healthz', views.healthz, name='healthz')
