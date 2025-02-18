``vc2_data_tables``
===================

The :py:mod:`vc2_data_tables` Python package contains machine-readable values
for the constants and data tables in the SMPTE ST 2042-series of standards
relating to the `VC-2 professional video codec
<https://www.bbc.co.uk/rd/projects/vc-2>`_.

Specifically, the values in this package are those defined in:

* `SMPTE ST 2042-1:2017 <ST2042-1_>`_ (VC-2)
* `SMPTE ST 2042-2:2017 <ST2042-2_>`_ (VC-2 Level Definitions)

.. _ST2042-1: https://ieeexplore.ieee.org/document/7967896
.. _ST2042-2: https://ieeexplore.ieee.org/document/8187792

These values may be used either via the :py:mod:`vc2_data_tables` Python module
or, in most cases, values may be read from CSV formatted data files located in
``vc2_data_tables/csv/*.csv``.

To read about the Python module, see :ref:`the module API documentation <api>`.

For an overview of the CSV formatting conventions see the :ref:`csvfiles`
documentation.

Finally, you can find the source code (and CSV data) for
:py:mod:`vc2_data_tables` `on GitHub
<https://github.com/bbc/vc2_data_tables/>`_.

.. only:: not latex

    .. note::
    
        This documentation is also `available in PDF format
        <https://bbc.github.io/vc2_data_tables/vc2_data_tables_manual.pdf>`_.

.. only:: not html

    .. note::
    
        This documentation is also `available to browse online in HTML format
        <https://bbc.github.io/vc2_data_tables/>`_.

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   api.rst
   csv_files.rst
