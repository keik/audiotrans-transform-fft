# -*- coding: utf-8 -*-


import pytest
import numpy as np
from audiotrans_transform_fft import FFTTransform


def test_accept_arg_of_verbose():
    FFTTransform(['-v'])  # no error would be raised


def test_accept_1D_float_array_and_return_1D_complex_array():
    tr = FFTTransform()
    data = np.array([1, 2, 3, 4, 5])
    transformed = tr.transform(data)

    assert transformed.dtype == 'complex64', \
        """transformed data is complex array"""
    assert transformed.shape == (data.shape[0] // 2 + 1,), \
        """transformed data is formed half of inputed array length"""


def test_not_accept_1D_str_array_and_raise_value_error():
    tr = FFTTransform()
    data = np.array(['a', 'b', 'c', 'd', 'e'])

    with pytest.raises(ValueError):
        tr.transform(data)
