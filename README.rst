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

WARNING: Please just one at a time for now. Does not handle multiple packages at this moment.

Just like `pip install` with the possibility to `--save` your required package.

.. code:: bash

    $ rqr install --save django

    {'django': '1.9.7'}

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
