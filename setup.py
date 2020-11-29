import re

from setuptools import setup

with open('src/webfin/__init__.py', encoding='utf8') as f:
    version = re.search(r"__version__ = '(.*?)'", f.read()).group(1)

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name='Webfin',
    version=version,
    install_requires=[
        'jinja2',
        'wtforms',
        'aiohttp',
        'aiohttp-swagger',
        'aiohttp_jinja2',
        'numpy',
        'scipy',
    ],
    extras_require={'test': ['pytest','pytest-mock', 'pytest-aiohttp','htmldom']},
)
