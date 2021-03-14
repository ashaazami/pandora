# Licensed under the MIT License.

# !/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import find_packages
from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pandora',
    version='1.0.0',
    description="",
    long_description=readme + '\n\n',
    author="Ashkan Aazami",
    author_email='',
    url='https://github.com/ashaazami/pandora',
    packages=find_packages(),
    package_dir={'pandora': 'pandora'},
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords=['mct'],
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ])
