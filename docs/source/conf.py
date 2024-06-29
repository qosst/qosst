# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "QOSST"
copyright = "2021-2024, Yoann Piétri, Matteo Schiavon, Valentina Marulanda Acosta, Baptiste Gouraud, Luis Trigo-Vidarte, Philippe Grangier, Amine Rhouni, Eleni Diamanti"
author = "Yoann Piétri, Matteo Schiavon, Valentina Marulanda Acosta, Baptiste Gouraud, Luis Trigo-Vidarte, Philippe Grangier, Amine Rhouni, Eleni Diamanti"
release = "0.10.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.bibtex",
    "sphinx_rtd_theme",
    "sphinx.ext.todo",
    "sphinx-prompt",
    "myst_parser",
    "sphinxcontrib.programoutput",
]
bibtex_bibfiles = ["refs.bib"]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

html_theme_options = {
    "logo_only": True,
    "display_version": True,
}
myst_heading_anchors = 3

intersphinx_mapping = {
    "qosst-core": ("https://qosst-core.readthedocs.io/en/latest", None),
    "qosst-hal": ("https://qosst-hal.readthedocs.io/en/latest", None),
    "qosst-alice": ("https://qosst-alice.readthedocs.io/en/latest", None),
    "qosst-bob": ("https://qosst-bob.readthedocs.io/en/latest", None),
    "qosst-skr": ("https://qosst-skr.readthedocs.io/en/latest", None),
    "qosst-sim": ("https://qosst-sim.readthedocs.io/en/latest", None),
}

root_doc = "index"
latex_documents = [
    (
        root_doc,
        "qosst.tex",
        "qosst",
        author.replace(", ", "\\and ").replace(" and ", "\\and and "),
        "manual",
    ),
]

latex_elements = {
    "preamble": r"""
\DeclareUnicodeCharacter{2588}{~}
\DeclareUnicodeCharacter{2557}{~}
\DeclareUnicodeCharacter{2554}{~}
\DeclareUnicodeCharacter{2550}{~}
\DeclareUnicodeCharacter{255D}{~}
\DeclareUnicodeCharacter{255A}{~}
\DeclareUnicodeCharacter{2551}{~}
\DeclareUnicodeCharacter{2584}{~}
\DeclareUnicodeCharacter{2580}{~}
"""
}

html_logo = "_static/qosst_logo_square_white.png"
