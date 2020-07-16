# -*- coding: utf-8 -*-

"""
Internal CSV table unpacking routines
=====================================

These routines are used to load and parse constants and tables of values from
CSV files into :py:class:`~enum.IntEnum` enums and dictionary-based tables.

See the documentation for an overview of the CSV conventions used.
"""

import re
import csv
import sys

from enum import IntEnum

from collections import OrderedDict, defaultdict


__all__ = [
    "is_ditto",
    "read_enum_from_csv",
    "read_lookup_from_csv",
    "read_quantisation_matrices_from_csv",
    "to_list",
    "to_enum_from_index",
    "to_enum_from_name",
    "to_dict_value",
]


def open_utf8(filename):
    """
    Open a UTF-8 text file for reading.

    Under Python 2, the file is intentionally opened with no encoding specified
    (files are treated as byte strings). Under Python 3, the file will be
    forced to be opened as UTF-8, regardless of the platform default (e.g.
    typically something silly under Windows).
    """
    if sys.version_info < (3, 0, 0):
        return open(filename)
    else:
        return open(filename, encoding="utf-8")


QUOTE_CHARS = [
    '"',  # ASCII double quote
    "“",  # Unicode double opening quote
    "”",  # Unicode double closing quote
    "'",  # ASCII single quote
    "’",  # Unicode single opening quote
    "’",  # Unicode single closing quote
    "`",  # ASCII tick
]
"""
The various unicode characters which spreadsheet programs (unhelpfully) replace
quotes with.

NB: Under Python 2, these strings are intentionally non-unicode strings (and so
will be interpreted as raw bytes) while in Python 3 these will be ordinary
unicode strings.
"""


def is_ditto(string):
    """Test if a cell's value string just indicates 'ditto'"""
    # NB: To enable backward compatibility with Python 2 (and its messy
    # handling of Unicode), this function works as if the input is a byte
    # string and avoids text-handling routines.
    
    quotes_removed = string
    for quote_char in QUOTE_CHARS:
        # This technically isn't a robust way to perform byte-wise unicode
        # character substitutions but given this simple application of just
        # detecting unicode quotes inserted by spreadsheet packages this is
        # excusable
        quotes_removed = quotes_removed.replace(quote_char, "")
    
    return quotes_removed != string and len(quotes_removed.strip()) == 0


def read_csv_without_comments(csv_filename):
    """
    Given a CSV, returns a list of dictionaries, one per row, containing the
    values in the CSV (as read by :py:class:`csv.DictReader`).
    """
    # Find the first non-empty/comment row in the CSV
    with open_utf8(csv_filename) as f:
        for first_non_empty_row, cells in enumerate(csv.reader(f)):
            if any(cell.strip() != "" and not cell.strip().startswith("#")
                   for cell in cells):
                break
    
    with open_utf8(csv_filename) as f:
        # Skip empty/comment rows
        for _ in range(first_non_empty_row):
            f.readline()
        
        return list(csv.DictReader(f))


def read_enum_from_csv(csv_filename, enum_name, module=None):
    """
    Create a :py:class:`IntEnum` class from the values listed in a CSV file.
    
    The 'name' field will be used as enum value names and the (integer) 'index'
    column will be used for values. Names must be unique, valid Python identifiers.
    
    Parameters
    ==========
    csv_filename : str
        Filename of the CSV file to read. Column headings will be read from the
        first row which isn't empty or contains only '#' prefixed values.
    enum_name : str
        The name of the :py:class:`IntEnum` class to be created.
    module : module
        (Optional) The Python module the returned enum will be defined in.
        Defaults to the caller's module (if this can be inferred
        automatically).
    
    Returns
    =======
    :py:class:`IntEnum`
    """
    rows = read_csv_without_comments(csv_filename)
    
    enum_values = OrderedDict()
    for row in rows:
        # Skip rows without names/indices
        if (not row["index"].strip() or is_ditto(row["index"]) or
                not row["name"].strip() or is_ditto(row["name"])):
            continue
        
        index = int(row["index"].strip())
        name = str(row["name"].strip())
        
        enum_values[name] = index
    
    
    if module is None:
        # Detect the module of the caller by inspecting the stack. This is a
        # bit gross, and won't work under all Python interpreters, but is what
        # enum.Enum also has to do and if its good enough for the stdlib, its
        # good enough for this...
        try:
            module = sys._getframe(1).f_globals["__name__"]
        except (AttributeError, ValueError, KeyError):
            pass
    
    return IntEnum(
        enum_name,
        enum_values,
        module=module,
    )


def read_lookup_from_csv(
    csv_filename,
    index_enum_type,
    namedtuple_type,
    type_conversions={},
):
    """
    Create a dictionary which looks up named tuples by :py:class:`IntEnum`
    enumerated indexes.
    
    Empty cells are treated as containing the same value as the previous row.
    Completely empty rows are ignored.
    
    Parameters
    ==========
    csv_filename : str
        Filename of the CSV file to read. Column headings will be read from
        the first row which isn't empty or contains only '#' prefixed values.
    index_enum_type : :py:class:`enum.IntEnum`
        The :py:class:`enum.IntEnum` which enumerates all of the valid index
        values. The index for each row will be taken from the 'index' column.
    namedtuple_type : :py:class:`collections.namedtuple`
        A namedtuple type which will be populated with the values for each row
        in the CSV.
    type_conversions : {column_name: func(str) -> value, ...}
        An optional converter function which will be used to convert each
        column's values from strings into some other type.
    
    Returns
    =======
    :py:class:`collections.OrderedDict` : {index: row_tuple, ...}
    """
    rows = read_csv_without_comments(csv_filename)
    
    column_values = defaultdict(str)
    
    lookup = OrderedDict()
    for row in rows:
        # Skip completely empty/comment-only rows
        if all(not cell.strip() or cell.strip().startswith("#")
               for key, cell in row.items()
               if key is not None):
            continue
        
        # Get values for this row (falling back on previous ones if absent)
        for field in namedtuple_type._fields + ("index", ):
            if row[field].strip() and not is_ditto(row[field]):
                column_values[field] = row[field]
        
        index = index_enum_type(int(column_values["index"]))
        
        value = namedtuple_type(**{
            field: type_conversions.get(field, str)(column_values[field])
            for field in namedtuple_type._fields
        })
        
        lookup[index] = value
    
    return lookup


def to_list(type_conversion):
    """
    Returns a function which takes a comma-separated string and returns a list
    of values converted by the supplied 'type_conversion' function.
    """
    def func(string):
        return [
            type_conversion(value)
            for value in filter(None, re.split(r"\s*,\s*", string))
        ]
    
    return func


def to_enum_from_index(enum_type):
    """
    Returns a function which maps strings containing enum value integers to
    their corresponding enum_type values.
    """
    def func(string):
        return enum_type(int(string))
    
    return func


def to_enum_from_name(enum_type):
    """
    Returns a function which maps strings containing enum value names to their
    corresponding enum_type values.
    """
    def func(string):
        return getattr(enum_type, string)
    
    return func

def to_dict_value(dictionary):
    """
    Returns a function which maps strings to their corresponding value in the
    supplied dictionary.
    """
    return dictionary.get


def read_quantisation_matrices_from_csv(csv_filename):
    """
    Read a table of preset quantisation matrices from a CSV.
    
    The CSV format is similar to (Table D.1) - (Table D.8).  The following
    columns will be present:
    
    * ``wavelet_index``: A wavelet transform index.
    * ``wavelet_index_ho``: A wavelet transform index.
    * ``dwt_depth_ho``: A horizontal-only transform index
    * ``level``: A transform level
    * ``orientations``: A comma-separated list of orientations (i.e. L, H, LL,
      HL, LH, HH)
    * Several columns named ``dwt_depth=n`` where ``n`` is an integer giving
      the dwt_depth the values in that column correspond to. The values in this
      column should be a comma-separated list of quantisation matrix values
      corresponding to the ``orientations`` specified for that row.
    
    Empty rows and rows containing only "#" prefixed cells are ignored. A cell
    which contains a ditto symbol (i.e. ``"``) will inherit the value of the
    cell above it.
    
    Parameters
    ==========
    csv_filename : str
        Filename of the CSV file to read.
    
    Returns
    =======
    quantisation_matrices : {(wavelet_index, wavelet_index_ho, dwt_depth, dwt_depth_ho): {level: {orientation: value, ...}, ...}, ...}
        Where:
        
        * ``wavelet_index`` and ``wavelet_index_ho`` are :py:class:`WaveletFilters`
          values
        * ``dwt_depth`` and ``dwt_depth_ho`` are transform depths (integers)
        * ``level`` is the transform level (integer)
        * ``orientation`` is one of `"L"`, `"H"`, `"LL"``, `"HL"``, `"LH"`` or `"HH"``
    """
    rows = read_csv_without_comments(csv_filename)
    last_row = defaultdict(str)
    quantisation_matrices = defaultdict(lambda: defaultdict(dict))
    for row in rows:
        # Skip completely empty/comment-only rows
        if all(not cell.strip() or cell.strip().startswith("#")
               for key, cell in row.items()
               if key is not None):
            continue
        
        # Back-fill row values with dittos
        for field in row:
            if is_ditto(row[field]):
                row[field] = last_row[field]
        last_row = row
        
        wavelet_index = int(row["wavelet_index"].strip())
        wavelet_index_ho = int(row["wavelet_index_ho"].strip())
        dwt_depth_ho = int(row["dwt_depth_ho"].strip())
        level = int(row["level"].strip())
        orientations = row["orientations"].split(",")
        
        for column_name in filter(
            lambda col: re.match(r"\s*dwt_depth\s*=\s*[0-9]+\s*", col),
            row,
        ):
            dwt_depth = int(column_name.partition("=")[2].strip())
            values = row[column_name].split(",")
            
            for orientation, value in zip(orientations, values):
                if value.strip():
                    quantisation_matrices[(
                        wavelet_index,
                        wavelet_index_ho,
                        dwt_depth,
                        dwt_depth_ho,
                    )][
                        level
                    ][
                        orientation.strip()
                    ] = int(value.strip())
    
    return quantisation_matrices
