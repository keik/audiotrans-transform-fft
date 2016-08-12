import numpy as np
from audiotrans import Transform


class FFTTransform(Transform):

    def __init__(self):
        pass

    def transform(self, data):
        return np.fft.fft(data)
