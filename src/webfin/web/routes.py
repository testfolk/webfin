import webfin

from . import views, apiv1


def setup_routes(app, prefix=''):
    # app.router.add_get(f'{prefix}/', index)
    app.router.add_get(f'{prefix}/optcalc', views.optcalc, name='optcalc')
    app.router.add_post(f'{prefix}/optcalc', views.optcalc, name='optcalc')
    app.router.add_post(f'{prefix}/calculate', views.calculate, name='calculate')


def setup_rest_routes(app, prefix=''):
    app.router.add_post(f'{prefix}/bsm/value', apiv1.value, name='value')
    app.router.add_post(f'{prefix}/bsm/vega', apiv1.vega, name='vega')
    app.router.add_get(f'{prefix}/healthz', apiv1.healthz, name='healthz')
