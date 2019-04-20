import time

import unicornhat as phat


class PhatDisplayer:
    def __init__(self, generate):
        self.generate_pixels = generate
        phat.set_layout(phat.AUTO)
        phat.rotation(0)
        phat.brightness(0.3)
        self.width, self.height = phat.get_shape()

    def set_generate(self, generate):
        self.generate_pixels = generate

    def run(self):
        while True:
            pixels = self.generate_pixels()
            self._set_pixels(pixels)
            time.sleep(0.02)

    def dispose(self):
        pass

    def _set_pixels(self, pixels):
        x = 0
        y = 0
        for pixel in pixels:
            r, g, b = pixel.rgb
            phat.set_pixel(x, y, r, g, b)
            x += 1
            if x == self.width:
                x = 0
                y += 1
            if y == self.height:
                break
        phat.show()
