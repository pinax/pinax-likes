import os
import sys

extensions = []
templates_path = []
source_suffix = '.rst'
master_doc = 'index'
project = u'phileo'
copyright = u'2013, Eldarion'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'default'
htmlhelp_basename = '%sdoc' % project
latex_documents = [
    ('index', '%s.tex' % project, u'%s Documentation' % project,
     u'Eldarion', 'manual'),
]
man_pages = [
    ('index', project, u'%s Documentation' % project,
     [u'Eldarion'], 1)
]

sys.path.insert(0, os.pardir)
m = __import__(project)

version = m.__version__
release = version
