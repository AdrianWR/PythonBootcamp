import numpy as np


class ColorFilter:

    @staticmethod
    def invert(array):
        return 1 - array
        
    @staticmethod
    def to_blue(array):
        blue = np.zeros(array.shape)
        blue[:, :, 2:] = array[:, :, 2:]
        return blue

    @staticmethod
    def to_green(array):
        return array * [0, 1, 0]

    def to_red(self, array):
        return array - self.to_green(array) - self.to_blue(array)

    @staticmethod
    def celluloid(array):
        return np.round(array)

    @staticmethod
    def to_grayscale(array, filter='w'):
        if filter == 'mean' or filter == 'm':
            sh = array.shape
            m = np.sum(array, axis=2)/3
            m = np.broadcast_to(m[..., None], sh)
            return m
        elif filter == 'weighted' or filter == 'w':
            w = np.sum(array * [0.299, 0.587, 0.114], axis=2)
            w = np.tile(w[..., None], 3)
            return w
