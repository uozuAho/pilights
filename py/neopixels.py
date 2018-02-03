from __future__ import print_function

try:
    from neopixel import *
    mock = False
except ImportError:
    print("No neopixel library found - will generate mock NeoPixels objects")
    mock = True


def new_instance(num_leds, max_brightness=40):
    pixels = NeoPixelsMock(num_leds) if mock else NeoPixels(num_leds)
    return NeoPixelWrapper(pixels, max_brightness)


class NeoPixelWrapper:

    def __init__(self, pixels, max_brightness=40):
        self.pixels = pixels
        self.max_brightness = max_brightness

    def set_all(self, r, g, b):
        r = self._limit(r)
        g = self._limit(g)
        b = self._limit(b)
        self.pixels.set_all(r, g, b)

    def _limit(self, x):
        return min(x, self.max_brightness)


class NeoPixels:

    def __init__(self, num_leds, output_pin=18, led_freq_hz=800000, dma=5,
                 invert=False, brightness=255):
        self.pixels = Adafruit_NeoPixel(num_leds, output_pin, led_freq_hz, dma,
            invert, brightness)
        self.pixels.begin()

    def set_all(self, r, g, b):
        """ Set all pixels to the given color """
        col = Color(r, g, b)
        for i in range(self.pixels.numPixels()):
            self.pixels.setPixelColor(i, col)
        self.pixels.show()


class NeoPixelsMock:

    def __init__(self, num_leds, output_pin=18, led_freq_hz=800000, dma=5,
                 invert=False, brightness=255):
        pass

    def set_all(self, r, g, b):
        print("Set all to ", r, g, b)
