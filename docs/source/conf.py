import os
import sys
import django

# Ajouter le chemin du projet pour que Sphinx puisse importer les modules Django
sys.path.insert(0, os.path.abspath('../..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'oc_lettings_site.settings'
django.setup()

# -- Project information -----------------------------------------------------
project = 'OC Lettings'
copyright = '2025, AUER Eric'
author = 'AUER Eric'
release = '1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',  # Pour documenter automatiquement le code Python
    'sphinx.ext.viewcode',  # Pour créer des liens vers le code source
    'sphinx.ext.napoleon',  # Pour le support des docstrings style Google/NumPy
]

templates_path = ['_templates']
exclude_patterns = []
language = 'fr'

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'  # Utilise le thème Read the Docs
html_static_path = ['_static']
