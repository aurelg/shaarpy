"""
Documentation
"""

from distutils.core import setup
from src.shaarpy import __version__

mod_name = 'shaarpy'
setup(name=mod_name,
      version=__version__,
      package_dir={'': 'src'},
      packages=['shaarpy'],
      package_data={},
      url='http://aurelien.latitude77.org',
      author='Aurelien Grosdidier',
      author_email='aurelien.grosdidier@gmail.com',
      requires=['requests', 'beautifulsoup4'])
