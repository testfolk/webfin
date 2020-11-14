======
WEBFIN
======

This project serves as a prototype for wrapping financial functions with python

Requirements
============

The project requires python3.6 or above.

Install
=======

Run the command below::

  pip install /path/to/project

Ideally, in a fresh virtual environment, which can be made using::

  python -m venv WEBFIN

Development
===========

To install in a development mode, do::

  pip install -e .

or::

  python setup.py develop


The project uses ``pytest`` for test runner, simply run ``tox`` in the project root directory.

Execute
=======

Installing the library would add a command ``webfin`` on the command line (or in the virtualenv if not installed globally)::

  usage: __main__.py [-h] [--pdb] {serve,web} ...

  WEBFIN CLI

  positional arguments:
    {serve,web}
      serve (web)
                web serve options

  optional arguments:
    -h, --help   show this help message and exit
    --pdb


To run the python api server do::

  webfin serve -H 127.0.0.1 -p 8080

Then navigate to `opt calc endpoint`_ for an option calculator or to the `swagger api`_

Alternatively, if you prefer to run the docker container, you will need to build it first::

  docker build . -t webfin


Then run::

  docker run -it -p8080:80 webfin

.. _`dev server`: http://127.0.0.1:8080
.. _`opt calc endpoint`: http://127.0.0.1:8080/optcalc
.. _`swagger api`: http://127.0.0.1:8080/api/v1/doc
