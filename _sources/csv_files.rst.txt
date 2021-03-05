.. _csvfiles:

CSV Files and Conventions
=========================

Many of the data tables exposed by this Python module are read from CSV files
contained in ``vc2_data_tables/csv/*.csv``. You are free to use these files
directly rather than via the :py:mod:`vc2_data_tables` module.

In general, the CSV files mimic the format which appears in the VC-2 standards
documents and can be opened in common spreadsheet packages and are intended to
be relatively human-readable.

.. tip::

    After opening the CSV files included with this module with a spreadsheet
    package it is often helpful to reset the width of all columns to a fixed
    size. This is because may files will contain comments which cause certain
    columns to be assigned very large sizes (see section about comments below).

.. warning::

    Take care when modifying these CSV files some spreadsheet packages contain
    unhelpful 'smart' features which can mangle cells containing values
    matching certain formats (e.g. anything which looks like a date). Also
    watch out for trailing spaces in cells.

The sections below define the specific conventions used by the CSV files in
this package.


CSV Dialect
-----------

The CSV provided use the Microsoft Excel CSV dialect and are encoded using
UTF-8. See Python's :py:mod:`csv` module for more background on CSV formatting
dialects.


Headings
--------

In all CSV files, the first non-empty/comment row contains headings for the
values beneath. The meanings of each column should be self-explantory, but
further hints may be given in the :py:mod:`vc2_data_tables` API documentation
associated with each table.

.. note::

    The :py:mod:`vc2_data_tables` software expects certain column names to be
    used but is insensitive to column order and will ignore any unexpected
    extra columns.


Comments
--------

To aid human consumption of the CSV data files, human-readable comments are
used. All rows in a CSV file containing only empty cells or cells whose values
start with a hash (``#``) character should be considered to be comments and
omitted.

The following illustrates how comments may be used in a CSV.

+------+-------------+-------------------+
| Not  | a           | comment!          |
+------+-------------+-------------------+
|      | # A comment | # Another comment |
+------+-------------+-------------------+
| Not  | a           | comment!          |
+------+-------------+-------------------+
| 123  | abc         | # *Not* a comment |
+------+-------------+-------------------+

.. warning::

    A cell starting with a hash (``#``) on a row which contains data is *not* a
    comment (see final row of the example above). Comments may only occur on
    rows which otherwise do not contain data.


Ditto
-----

In some tables, values from previous rows may be repeated using 'ditto',
written as ``"`` or ``''``. For example:

+--------+----------+
| Number | Above 3? |
+========+==========+
| 1      | No       |
+--------+----------+
| 2      | "        |
+--------+----------+
| 3      | "        |
+--------+----------+
| 4      | Yes      |
+--------+----------+
| 5      | "        |
+--------+----------+
| 6      | "        |
+--------+----------+

.. warning::

    Excel and other spreadsheet packages often replace 'straight' quote
    characters with their 'curly' unicode variants. Take care when manually
    parsing CSV files containing ditto to also handle these variants.


Lists
-----

Occasionally table cells may contain a comma separated list of values. These
commas are escaped according to the Excel CSV convention of enclosing the whole
cell value in double quotes.
