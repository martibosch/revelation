#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""revelation setup file"""

from io import open  # compatible enconding parameter
from os import path

from setuptools import find_packages, setup

__version__ = '0.5.2'

classifiers = [
    "Environment :: Console",
    "Environment :: Web Environment",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Natural Language :: English",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Topic :: Multimedia :: Graphics :: Presentation",
    "Topic :: Text Processing :: Markup :: HTML",
]

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

# get the dependencies for testing and dev mode
with open(path.join(here, 'requirements-dev.txt'), encoding='utf-8') as f:
    test_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [
    x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')
]

setup(
    name='revelation',
    version=__version__,
    description="Make awesome reveal.js presentations with revelation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Martí Bosch',
    author_email='marti.bosch@epfl.ch',
    url="https://github.com/humrochagf/revelation",
    license="GPL-3.0",
    packages=find_packages(),
    package_data={'revelation': ["templates/presentation.html"]},
    zip_safe=False,
    install_requires=install_requires,
    dependency_links=dependency_links,
    entry_points=dict(console_scripts=["revelation=revelation.cli:cli"]),
    platforms="any",
    keywords="presentation slides reveal.js markdown",
    classifiers=classifiers,
    test_suite="tests",
    tests_require=test_reqs,
    extras_require={"test": test_reqs},
)
