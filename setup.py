#!/usr/bin/env python

from setuptools import setup, find_packages

REQUIRED_PACKAGES = [
    'pyes'
]

setup(
    name='pyes-geohash-facet',
    version='1.0',
    description=('pyes plugin for the geohash facet '
                 '(https://github.com/triforkams/geohash-facet)'),
    author='Przemyslaw Kaminski',
    packages=find_packages(),
    install_requires=REQUIRED_PACKAGES,
 )
