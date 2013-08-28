#! /usr/bin/env python
'''Cairoplot installation script.'''

from setuptools import setup

import cairoplot

setup(
    name='cairoplot',
    version=cairoplot.__version__,
    url='http://rodrigoaraujo01.github.com/cairoplot/',
    license='GNU LGPL 2.1',
    author='Rodrigo Araujo',
    author_email='alf.rodrigo@gmail.com',
    description='Cairoplot',
    long_description='''
        Using Python and PyCairo to develop a module to plot graphics in an
        easy and intuitive way, creating beautiful results for presentations,
        websites and papers.
        ''',
    packages=['cairoplot'],
    platforms='any',
    test_suite='test.test_all'
)
