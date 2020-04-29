from ImageProcessor import ImageProcessor
from ScrapBooker import ScrapBooker

if __name__ == "__main__":
    ip = ImageProcessor()
    sp = ScrapBooker()
    img = ip.load('42AI.png')
    # img = sp.crop(img, (100, 100), (0,0))
    # ip.display(sp.crop(img, (500, 500)))
    # ip.display(sp.crop(img, (50, 50), (50, 50)))
    # ip.display(sp.crop(img, (1, 1), (199, 199)))
    # ip.display(sp.thin(img, 2, 0))
    # ip.display(sp.thin(img, 2, 1))
    # ip.display(sp.juxtapose(img, 4, 0))
    # ip.display(sp.juxtapose(img, 2, 1))
    # ip.display(sp.juxtapose(img, 1, 1))
    # ip.display(sp.juxtapose(img, 0, 1))
    ip.display(sp.mosaic(img, (4, 4)))
