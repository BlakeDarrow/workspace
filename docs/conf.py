# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Workspace'
copyright = '2025, Blake Darrow'
author = 'Blake Darrow'

version = '1.0'
release = '1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'piccolo_theme'
html_static_path = ['static']
html_short_title = "Blake Darrow"
html_theme_options = {

    "show_theme_credit": False,
    "source_url": 'https://github.com/BlakeDarrow/workspace'
}
