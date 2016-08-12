#!/usr/bin/env python
# -*- coding: utf-8 -*-

import audiotrans_transform_fft
from setuptools import setup, find_packages

install_requires = [
    'numpy',
    'audiotrans'
]

setup(name='audiotrans-transform-fft',
      version=audiotrans_transform_fft.__version__,
      description=audiotrans_transform_fft.__desc__,
      author=audiotrans_transform_fft.__author__,
      author_email=audiotrans_transform_fft.__author_email__,
      url=audiotrans_transform_fft.__url__,
      packages=find_packages(),
      install_requires=install_requires)
