#!/usr/bin/env python
import sys
from setuptools import setup, find_packages

from dbudget import __version__

setup(
    name='dbudget',
    version=__version__,
    packages=find_packages(exclude=('tests',)),
    license='GPLv3',
    py_modules=[''],
    author='Sinuhe Tellez',
    author_email='dubyte@gmail.com',
    description='dubyte budget',
    keywords='budget cli',
    test_suite='unittests',
    requires=['prompt_toolkit', 'transitions'],
)
