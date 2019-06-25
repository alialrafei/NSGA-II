# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------------------
# author     = "Sameh K. Mohamed"
# copyright  = "Copyright 2019, The Project"
# credits    = ["Sameh K. Mohamed"]
# license    = "MIT"
# version    = "0.0.0"
# maintainer = "Sameh K. Mohamed"
# email      = "sameh.kamaleldin@gmail.com"
# status     = "Development"
# -----------------------------------------------------------------------------------------
# Created by sameh at 2019-06-25
# -----------------------------------------------------------------------------------------
# file description:
# setup file
# -----------------------------------------------------------------------------------------

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
from libevolve import __version__ as lib_ver

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='libevolve',
    version=lib_ver,  # Required
    description='A python library for evolutionary algorithms',
    long_description=long_description,
    url='https://github.com/uniopt/libevolve',
    author='UniOpt',
    author_email='sameh.kamaleldin@gmail.com',
    keywords='genetic algorithms optimisation',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[],
    extras_require={
        'dev': ['pytest', 'sphinx'],
        'test': ['pytest'],
    }
)