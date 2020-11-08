import argparse
from aiohttp_swagger import setup_swagger
import logging
import pdb
import sys
import traceback
import aiohttp_jinja2
import jinja2
from aiohttp import web
import webfin
from webfin.web.routes import setup_routes


def attach_debugger():
    """drop to pdb (or better pdbpp) on errors"""
    def info(type, value, tb):
        if hasattr(sys, 'ps1') or not sys.stderr.isatty():
            sys.__excepthook__(type, value, tb)
        else:
            traceback.print_exception(type, value, tb)
            pdb.post_mortem(tb)

    sys.excepthook = info


async def init_app(argv=None):
    app = web.Application()
    aiohttp_jinja2.setup(app,
                         loader=jinja2.FileSystemLoader('/webfin/src/webfin/web/templates'))
    # setup views and routes
    setup_routes(app, '/api/v1')
    swagger_path = webfin.root_dir / 'web' / 'opendoc.yaml'
    setup_swagger(app, swagger_url="/api/v1/doc", swagger_from_file=swagger_path)
    # setup_swagger(app, swagger_url="/api/v1/doc", ui_version=2)
    return app


def serve_parser_cli(args):
    logging.basicConfig(level=logging.DEBUG)
    app = init_app(args)
    web.run_app(app, host=args.host, port=args.port)


def cli():
    parser = argparse.ArgumentParser(description="WEBFIN CLI")
    parser.add_argument('--pdb', required=False, action='store_true')
    # collection of shared options
    shared_parser = argparse.ArgumentParser(add_help=False)
    shared_parser.add_argument('--pdb', required=False, action='store_true')
    shared_parser.add_argument('--verbose', '-v', default=1, action='count')
    subparsers = parser.add_subparsers(dest='command')
    # server parser
    serve_parser = subparsers.add_parser('serve', parents=[shared_parser], aliases=['web'],
                                         help="web serve options")
    serve_parser.add_argument('--host', '-H', action='store', default='localhost',
                              help="interface to bind on")
    serve_parser.add_argument('--port', '-p', action='store', default=8080,
                              help="port to listen to")
    serve_parser.set_defaults(func=serve_parser_cli)
    # handle actual options
    args = parser.parse_args()
    if args.command is None:
        parser.print_help()
        sys.exit(1)
    return args


def main():
    args = cli()
    if 'pdb' in args and args.pdb:
        attach_debugger()
    args.func(args)


if __name__ == '__main__':
    main()
