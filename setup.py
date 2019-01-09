#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import os

from setuptools import setup, find_packages

try:
    with open('README.rst') as f:
        readme = f.read()
except IOError:
    readme = ''

def _requires_from_file(filename):
    return open(filename).read().splitlines()

# version
here = os.path.dirname(os.path.abspath(__file__))
version = next((line.split('=')[1].strip().replace("'", '')
                for line in open(os.path.join(here,
                                              'pcd2kml',
                                              '__init__.py'))
                if line.startswith('__version__ = ')),
               '0.0.dev4')

setup(
    name="pcd2kml",
    version=version,
    url='https://github.com/tier4/pcd2kml',
    author='kikkakesan',
    author_email='kikkakesan@gmail.com',
    maintainer='tier4',
    maintainer_email='',
    description='Package Dependency: Validates package requirements',
    long_description=readme,
    packages=find_packages(),
    install_requires=["simplekml", "scipy", "numpy"],
    license="MIT",
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      pkgdep = pcd2kml.scripts.command:main
    """,
)