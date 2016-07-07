rqr
===

Python ReQuiRements.

Handle requirements for python. Based on pip, inspired by npm. And get rid of all those different requirements.txt files.

WARNING: This is alpha and a pure prototype at the moment.

Installation
------------

.. code:: bash

    $ pip install rqr

Usage
-----

Install
~~~~~~~

Just like `pip install` with the possibility to `--save` your required package.

.. code:: bash

    $ rqr install --save django ipython

    {'django': '1.9.7', 'ipython: '4.2.1'}

Does also support `--save-development` and `--save-production`. Default is `base` which is shared across the other two.


List
~~~~

Shows all managed requirements, just like `pip list`.

.. code:: bash

    $ rqr list

    base:
      - django@1.9.7
    development:
      - ipython@4.2.1

Migrate
~~~~~~~

WARNING: Does override your `rqr.yaml` configuration if you had one before without any further warning.

Tries to discover existing `requirements` files or folders and migrate them. Uses current working directory and does not traverse directories deeply.

.. code:: bash

    $ rqr migrate

    Discovered dev-requirements.txt (development)
    Discovered requirements/base.txt (base)
      - django@1.9.3
      - djangorestframework@3.3.1
      - pillow@3.1.1
    Discovered requirements/development.txt (development)
      - Invalid: -r base.txt
      - ipython@4.0.0
    Discovered requirements/production.txt (production)
      - Invalid: -r base.txt
      - gunicorn@19.3.0
    Discovered requirements-dev.txt (development)
    Discovered requirements.txt (base)
