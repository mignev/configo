#!/usr/bin/env python

from __future__ import with_statement
from configo import version as configo_version
import distutils.core
import os

# Importing setuptools adds some features like "setup.py develop", but
# it's optional so swallow the error if it's not there.
try:
    import setuptools
except ImportError:
    pass

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

distutils.core.setup(name='Configo',
      version=configo_version,
      description='Easy way to use existing JSON, XML or YAML config files from bash shell/scripts',
      author='Marian Ignev',
      author_email='m@ignev.net',
      url='http://m.ignev.net/code/configo',
      packages=['configo'],
      long_description=read('README.md'),
      package_dir={"configo":"configo"},
      install_requires = ['pyyaml'],
      scripts= ["bin/configo"],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Operating System :: POSIX',
          'Operating System :: POSIX :: BSD',
          'Operating System :: POSIX :: Linux',
          'Operating System :: Unix',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Topic :: System :: Shells',
          'Topic :: Text Processing :: Markup :: XML',
          'Topic :: Utilities',
          ],
     )
