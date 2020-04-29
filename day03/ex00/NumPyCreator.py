#!/usr/bin/python3
import numpy as np


class NumPyCreator:

    def from_list(self, list):
        return np.array(list)

    def from_tuple(self, tup):
        return np.array(tup)

    def from_iterable(self, it):
        return np.fromiter(it, float)

    @staticmethod
    def from_shape(shape, value=0):
        return np.full(shape, value)

    @staticmethod
    def random(*shape):
        return np.random.rand(*shape)

    @staticmethod
    def identity(n):
        return np.identity(n)


if __name__ == "__main__":
    npc = NumPyCreator()
    print(npc.from_shape((2, 3), 9))
    print(npc.random(3, 3))
    print(npc.identity(4))
