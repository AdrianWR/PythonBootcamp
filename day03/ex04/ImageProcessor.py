#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class ImageProcessor:

    @staticmethod
    def load(path):
        img = np.array(mpimg.imread(path))
        dim = np.shape(img)
        print(f"Image dimensions: {dim[0]} x {dim[1]}")
        return img

    @staticmethod
    def display(array):
        plt.imshow(array)
        plt.show()
        pass


if __name__ == "__main__":
    ip = ImageProcessor()
    img = ip.load("42AI.png")
    ip.display(img)
