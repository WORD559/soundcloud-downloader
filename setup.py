#!/usr/bin/env python
# coding: utf-8
import codecs
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

with codecs.open('README.md') as file:
    long_description = file.read()
    if not isinstance(long_description, str):
        long_description = str(long_description, 'utf-8')


setup(
    name='sc_downloader',
    version='0.1.0',
    description='Downloads music from Soundcloud.',
    long_description=long_description,
    author='WORD559',
    author_email='josh.barrass.work@gmail.com',
    url='https://github.com/WORD559/snapchat-downloader',
    scripts=['soundcloud-dl'],
    packages=['soundcloud'],
    package_dir={
        'soundcloud': 'soundcloud',
        },
    install_requires=['requests', 'docopt>=0.5.0'],
    keywords='soundcloud downloader music archive dump',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
    ]
)