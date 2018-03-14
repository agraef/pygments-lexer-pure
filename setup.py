#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

version = '0.2'
long_description = open('README.rst').read();

classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: Plugins',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

setup(
    name='pygments-lexer-pure',
    version=version,
    description='Pygments lexer for the Pure programming language.',
    long_description=long_description,
    classifiers=classifiers,
    keywords=['pygments', 'lexer', 'pure', 'syntax highlighting'],
    author='Albert Graef',
    author_email='aggraef at gmail dot com',
    url='https://github.com/shkumagai/pygments-style-solarized',
    license='MIT',
    packages=find_packages(),
    install_requires=['pygments >= 1.5'],
    entry_points="""
        [pygments.lexers]
        Pure=pure_lexer.pure:PureLexer
    """,
    zip_safe=False,
)
