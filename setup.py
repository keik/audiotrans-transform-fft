#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

install_requires = [
    'numpy',
    'audiotrans'
]

dependency_links = [
    'https://github.com/keik/audiotrans.git'
]

setup(name='audiotrans-transform-fft',
      version='0.0.1.dev0',
      description="""audiotrans transform module to FFT""",
      author='keik',
      author_email='k4t0.kei@gmail.com',
      url='https://github.com/keik/audiotrans-transform-fft',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Intended Audience :: Developers',
          'Topic :: Multimedia :: Sound/Audio :: Conversion',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
      ],
      packages=find_packages(),
      install_requires=install_requires,
      dependency_links=dependency_links)
