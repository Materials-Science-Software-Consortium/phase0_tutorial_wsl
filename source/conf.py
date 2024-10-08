# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'PHASE/0 チュートリアル'
copyright = '2024, PHASEシステム研究会'
author = 'PHASEシステム研究会'

# The full version, including alpha/beta/rc tags
release = '2024.01'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
#'sphinxcontrib.rsvgconverter',
#'sphinxcontrib.inkscapeconverter'
#'sphinxcontrib.cairosvgconverter'
#'sphinx.ext.imgconverter'
]
#inkscape_converter_bin = '/usr/bin/inkscape'
#rsvg_converter_args = ['-a']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'ja'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

numfig = True
numtable = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
#html_style = "css/phase0.css"
#html_logo='cover/images/image1.png'
#latex_logo='cover/images/image1.png'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

from sphinx.highlighting import PygmentsBridge
from pygments.formatters.latex import LatexFormatter

class CustomLatexFormatter(LatexFormatter):
    def __init__(self, **options):
        super(CustomLatexFormatter, self).__init__(**options)
        self.verboptions = r"formatcom=\small"

PygmentsBridge.latex_formatter = CustomLatexFormatter

latex_elements = {
        'preamble': r''' \usepackage{braket} '''
}
rst_prolog=u"""
.. |PHASE020XX.YY| replace:: phase0_2024.01
"""

master_doc = 'index'
#latex_engine = 'uplatex'
