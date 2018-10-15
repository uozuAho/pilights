import sys

sys.path.append('..')

from presenter import Pixel


class PixelGeneratorSlave:
    """ Implements presenter.generator, and includes methods for real-time control """
    def __init__(self, num_pixels):
        self.pixels = [Pixel() for i in range(num_pixels)]

    def generate(self):
        return self.pixels

    def set_all(self, r, g, b):
        for p in self.pixels:
            p.rgb[0] = r
            p.rgb[1] = g
            p.rgb[2] = b
