from __future__ import print_function

try:
    from neopixel import *
    mock = False
except ImportError:
    print("No neopixel library found - will generate mock NeoPixels objects")
    mock = True


def new_instance(num_leds):
    if mock:
        return NeoPixelsMock(num_leds)
    else:
        return NeoPixels(num_leds)


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
