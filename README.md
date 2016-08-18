# audiotrans-transform-fft

[![License](https://img.shields.io/pypi/l/audiotrans-transform-fft.svg?style=flat-square)](https://github.com/keik/audiotrans-transform-fft/blob/master/LICENSE)
[![Python](https://img.shields.io/pypi/pyversions/audiotrans-transform-fft.svg?style=flat-square)](https://pypi.python.org/pypi/audiotrans-transform-fft)
[![PyPI](https://img.shields.io/pypi/v/audiotrans-transform-fft.svg?style=flat-square)](https://pypi.python.org/pypi/audiotrans-transform-fft)
[![Travis CI](https://img.shields.io/travis/keik/audiotrans-transform-fft.svg?style=flat-square)](https://travis-ci.org/keik/audiotrans-transform-fft)
[![Coverage Status](https://img.shields.io/coveralls/keik/audiotrans-transform-fft.svg?style=flat-square)](https://coveralls.io/github/keik/audiotrans-transform-fft)

[audiotrans](https://github.com/keik/audiotrans) transform module to FFT


## Installation

```
pip install audiotrans-transform-fft
```


## Usage

As `audiotrans` transform module, like

```
audiotrans <filepath> -t fft -v -c spec
```

Options of the below is available through subarg (like `[ foo -h ]`)

```
usage: fft [-h] [-v]

audiotrans transform module for FFT

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  Run as verbose mode
```


## Test

```
make test
```


## License

MIT (c) keik
