SMPTE ST 2042-1 (VC-2) Constants and Data Tables
================================================

**This repository is a work-in-progress.**

This Python package, ``vc2_data_tables``, contains machine-readable versions of
the constants and data tables in the SMPTE ST 2042-series of standards relating
to the `VC-2 professional video codec
<https://www.bbc.co.uk/rd/projects/vc-2>`_.


Installation
------------

(**Coming soon...**) You can install the ``vc2_data_tables`` Python module from
`PyPI <https://pypi.org/>`_ using::

    $ pip install vc2_data_tables

Alternatively you can install it from a copy of this repository using::

    $ python setup.py install

If you just want the data in CSV format, go to the `vc2_data_tables/csv
<./vc2_data_tables/csv>`_ directory.


Tests
-----

To run the test suite for the data loading routines, first install the test
suite dependencies using::

    $ pip install -r requirements-test.txt

Then run the tests::

    $ pytest tests/

To automatically run the test suite under several versions of Python ``tox``
may be used::

    $ pip install tox
    $ tox


Documentation
-------------

To build the documentation, first install the build dependencies::

    $ pip install -r requirements-doc.txt

Then build the documentation::

    $ cd docs
    $ make html  # or make latexpdf 

The built (HTML) documentation can be found in `docs/build/html/index.html
<./docs/build/html/index.html>`_.


Author
------

This module is currently being developed by `Jonathan Heathcote
<mailto:jonathan.heathcote@bbc.co.uk>`_ from BBC R&D as part of a project to
refresh VC-2's conformance testing procedures.
