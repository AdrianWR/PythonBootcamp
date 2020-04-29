#!/usr/bin/python3
import numpy as np


class ScrapBooker:

    @staticmethod
    def crop(array, dimensions, position=(0, 0)):
        p = position
        d = tuple(i if i < j else j for i, j, in zip(dimensions, array.shape))
        if any(True for i, j in zip(d, dimensions) if dimensions > d):
            print("Dimensions out of bounds. Cropped to max size.")
        return array[p[1]: p[1] + d[1], p[0]: p[0] + d[0]]

    @staticmethod
    def thin(array, n, axis):
        if axis == 1:
            array = array.transpose((1, 0, 2))
        th = [j for i, j in enumerate(array) if i % n != 0]
        th = np.array(th)
        return th if axis == 0 else th.transpose((1, 0, 2))

    @staticmethod
    def juxtapose(array, n, axis):
        jp = array
        while n - 1 > 0:
            jp = np.concatenate((jp, array), axis)
            n -= 1
        return jp

    def mosaic(self, array, dimensions):
        mos = self.juxtapose(array, dimensions[0], 0)
        mos = self.juxtapose(mos, dimensions[1], 1)
        return mos
