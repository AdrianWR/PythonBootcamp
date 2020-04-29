from ImageProcessor import ImageProcessor
from AdvancedFilter import AdvancedFilter

if __name__ == "__main__":
    ip = ImageProcessor()
    af = AdvancedFilter()
    img = ip.load('doge.png')
    ip.display(img)
    ip.display(af.mean_blur(img))
    #ip.display(cf.to_blue(img))
    #ip.display(cf.to_green(img))
    #ip.display(cf.to_red(img))
    #ip.display(cf.celluloid(img))
    #ip.display(cf.to_grayscale(img, 'm'))
    #ip.display(cf.to_grayscale(img))
