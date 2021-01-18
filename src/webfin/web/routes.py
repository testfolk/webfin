from webfin import root_dir

from . import apiv1, views


def setup_routes(app, prefix=''):
    # app.router.add_get(f'{prefix}/', index)
    app.router.add_get(f'{prefix}/optcalc', views.optcalc, name='optcalc')
    app.router.add_post(f'{prefix}/optcalc', views.optcalc, name='optcalc')
    setup_static_routes(app)


def setup_rest_routes(app, prefix=''):
    app.router.add_post(f'{prefix}/bsm/value', apiv1.value, name='value')
    app.router.add_post(f'{prefix}/bsm/vega', apiv1.vega, name='vega')
    app.router.add_get(f'{prefix}/healthz', apiv1.healthz, name='healthz')


def setup_static_routes(app, prefix=''):
    app.router.add_static(f'{prefix}/static/',
                          path=root_dir / 'web' / 'static',
                          name='static')
