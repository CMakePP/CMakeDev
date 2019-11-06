# -*- coding: utf-8 -*-
# -- Project information -----------------------------------------------------

project = u'CMakeDev'
copyright = u'2019, Ryan M. Richard'
author = u'Ryan M. Richard'

# The short X.Y version
version = u'1.0.0'
# The full version, including alpha/beta/rc tags
release = u'1.0.0alpha'

# -- Path setup --------------------------------------------------------------

import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0,dir_path)
doc_path = os.path.dirname(dir_path)
root_path = os.path.dirname(doc_path)
build_path = os.path.join(doc_path, "build")

# -- General configuration ---------------------------------------------------
highlight_language = 'cmake'
templates_path = ['.templates']
source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'sphinx_rtd_theme'
html_static_path = []
htmlhelp_basename = project + 'doc'
extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.githubpages',
]

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
}


latex_documents = [
    (master_doc, project + '.tex', project+ u'Documentation', author, 'manual'),
]

man_pages = [
    (master_doc,project, project+ u'Documentation', [author], 1)
]

texinfo_documents = [
    (master_doc, project, project + u'Documentation', author, project,
     'One line description of project.', 'Miscellaneous'),
]
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


