# Configuration file for the Sphinx documentation builder.

import os
import sys


# -- Path setup --------------------------------------------------------------

# To find the vc2_data_tables module
sys.path.insert(0, os.path.abspath("../.."))


# -- Project information -----------------------------------------------------

project = "SMPTE ST 2042-1 (VC-2) Data Tables"
copyright = "2021, BBC"
author = "BBC"

from vc2_data_tables import __version__ as version
release = version

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.doctest",
    "sphinx.ext.mathjax",
    "numpydoc",
]

# -- Options for numpydoc/autodoc --------------------------------------------

# Fixes autosummary errors
numpydoc_show_class_members = False

autodoc_member_order = "bysource"

add_module_names = False

autodoc_default_flags = [
    "members",
    "undoc-members",
]

# -- Options for intersphinx -------------------------------------------------

intersphinx_mapping = {
    "python": ("http://docs.python.org/3", None),
}


# -- Options for HTML output -------------------------------------------------

html_theme = "nature"

html_static_path = ["_static"]


# -- Options for PDF output --------------------------------------------------

latex_elements = {
    "papersize": "a4paper",
    # Add an 'Introduction' chapter heading to the content which appears before
    # all of the main chapters.
    "tableofcontents": r"""
        \sphinxtableofcontents
        \chapter{Introduction}
    """,
    # Make index entries smaller since some are quite long
    "printindex": r"\footnotesize\raggedright\printindex",
}

# Show page numbers in references
latex_show_pagerefs = True

# Show hyperlink URLs in footnotes
latex_show_urls = "footnote"

# Don't include a module index (the main index should be sufficient)
latex_domain_indices = False
