# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
from pathlib import Path

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = "ACTRIS-CCRES documentation"
copyright = "2024, ACTRIS-CCRES"
author = "ACTRIS-CCRES"
release = "1.0"

BASE_URL = "https://github.com/ACTRIS-CCRES/docs"
LOGO_PATH = Path(__file__).parent / "assets" / "logo_actris_ccress.png"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.linkcode",
    "myst_parser",
]


def linkcode_resolve(domain, info):
    if domain != "py":
        return None
    if not info["module"]:
        return None
    filename = info["module"].replace(".", "/")
    return f"{BASE_URL}/tree/main/{filename}.py"


autosummary_generate = True

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True


autodoc_default_options = {
    "members": True,
    "show-inheritance": True,
}

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

templates_path = ["_templates"]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

suppress_warnings = ["myst.domains", "ref.ref"]

myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    "fieldlist",
    "html_admonition",
    "html_image",
    "colon_fence",
    "smartquotes",
    "replacements",
    # "linkify",
    "strikethrough",
    "substitution",
    "tasklist",
    "attrs_inline",
    "attrs_block",
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme_options = {
    "repository_url": BASE_URL,
    "use_repository_button": True,
    "use_issues_button": True,
    "use_download_button": True,
    "use_sidenotes": True,
    "home_page_in_toc": False,
    "show_toc_level": 2,
}

html_theme = "sphinx_book_theme"
html_static_path = ["assets", "_static"]
# html_css_files = [
#     "css/custom.css",
# ]
html_logo = str(LOGO_PATH)
