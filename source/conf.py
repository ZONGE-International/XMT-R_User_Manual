# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'XMT-R User Manual'
copyright = '2024, ZONGE International'
author = 'ZONGE International'
release = '01'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

#extensions = ['sphinx.ext.imgmath']
extensions = ['sphinx.ext.mathjax']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ["custom.css"]  # contains special formating used in the R&D documentation
html_favicon = 'zonge.ico'
html_logo = 'Zonge_logo_white_transparent.png'
html_theme_options = {
'logo_only': True,
 'display_version': False,
}