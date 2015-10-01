import os
import sys

extensions = []
templates_path = []
source_suffix = '.rst'
master_doc = 'index'
project = u'likes'
copyright = u'2014, James Tauber and Contributors'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'default'
htmlhelp_basename = '%sdoc' % project
latex_documents = [
    ('index', '%s.tex' % project, u'%s Documentation' % project,
     u'Pinax', 'manual'),
]
man_pages = [
    ('index', project, u'%s Documentation' % project,
     [u'Pinax'], 1)
]

sys.path.insert(0, os.pardir)
m = __import__(project)

version = m.__version__
release = version
