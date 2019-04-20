import sys
from threading import Thread

sys.path.append('..')

from light_drivers.interfaces import Pixel
import pixel_patterns.pixel_strip_patterns as patterns


class PixelService:
    """ Deals with all pixel stuff required by the flask app """
    def __init__(self, num_pixels):
        self.num_pixels = num_pixels
        self.generator = ConstantValueGenerator(self.num_pixels)

    def start_displayer(self, device):
        if device == 'pygame':
            from light_drivers.pygame_pixels.pygame_pixels import PygamePixelDisplayer
            pixeldisp = PygamePixelDisplayer(self._generate)
        elif device == 'arduino':
            from light_drivers.arduino_pixels.py_serial_pixels.serial_pixel_displayer import SerialPixelDisplayer
            pixeldisp = SerialPixelDisplayer(self._generate)
        elif device == 'phat':
            from light_drivers.phat_pixels.phat_displayer import PhatDisplayer
            pixeldisp = PhatDisplayer(self._generate)
        else:
            raise Exception('unknown displayer device: ' + device)

        # run the displayer in a background thread, since it runs a blocking loop
        dispthread = Thread(target=pixeldisp.run)
        dispthread.start()

    def set_all(self, r, g, b):
        self.generator = ConstantValueGenerator(self.num_pixels)
        self.generator.set_all(r, g, b)

    def set_pattern(self, name):
        self.generator = PatternGenerator(self.num_pixels)
        self.generator.set_pattern(name)

    def _generate(self):
        return self.generator.generate()


class ConstantValueGenerator:
    def __init__(self, num_pixels):
        self.pixels = [Pixel() for i in range(num_pixels)]

    def generate(self):
        return self.pixels

    def set_all(self, r, g, b):
        for p in self.pixels:
            p.rgb[0] = r
            p.rgb[1] = g
            p.rgb[2] = b


class PatternGenerator:
    def __init__(self, num_pixels):
        self.num_pixels = num_pixels
        self.patterns = {
            'rainbow': lambda: patterns.Rainbow(self.num_pixels),
            'colorwipe': lambda: patterns.ColorWiper(self.num_pixels, Pixel(100, 0, 100), 50),
            'rainbow_cycle': lambda: patterns.RainbowCycle(self.num_pixels),
            'theatre': lambda: patterns.TheatreChaser(self.num_pixels, Pixel(100, 0, 100), 50)
        }
        self.generator = self._get_generator('rainbow')

    def set_pattern(self, name):
        self.generator = self._get_generator(name)

    def generate(self):
        return self.generator.generate()

    def _get_generator(self, name):
        return self.patterns[name]()
