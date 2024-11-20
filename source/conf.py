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
    "linkify",
    "strikethrough",
    "substitution",
    "tasklist",
    "attrs_inline",
    "attrs_block",
]
myst_linkify_fuzzy_links = False

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
    "extra_footer": """
    <div style="display: flex; justify-content: space-between;" >
        <a href="https://www.cnrs.fr">
            <img src="_static/institutions/logo_cnrs.png" alt="CNRS logo" height="50px">
        </a>
        <a href="https://www.uvsq.fr/">
            <img src="_static/institutions/logo_uvsq.png" alt="UVSQ logo" height="50px">
        </a>
        <a href="https://www.polytechnique.fr/">
            <img src="_static/institutions/logo_polytechnique.png" alt="polytechnique logo" height="50px">
        </a>
        <a href="https://www.fmi.fi/">
            <img src="_static/institutions/logo_fmi.png" alt="FMI logo" height="50px">
        </a>
        <a href="https://www.tudelft.nl/en/">
            <img src="_static/institutions/logo_tu-delft.png" alt="TU-delft logo" height="50px">
        </a>
        <a href="https://www.uni-koeln.de/">
            <img src="_static/institutions/logo_uni-koln.jpg" alt="uni koln logo" height="50px">
        </a>
    </div>
    """,
}

html_last_updated_fmt = "%b %d, %Y"

html_theme = "sphinx_book_theme"
html_static_path = ["assets", "_static"]
html_favicon = str(LOGO_PATH)
html_logo = str(LOGO_PATH)
