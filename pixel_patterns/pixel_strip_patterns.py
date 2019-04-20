import sys
import time

sys.path.append('..')

from light_drivers.interfaces import Pixel


NUM_PIXELS = 40


class BunchOfPatterns: # implements Generator

    def __init__(self):
        self.last_change_time = 0
        self.current_generator = RainbowCycle(NUM_PIXELS)
        self.generator_idx = 0
        self.generators = [
            lambda: ColorWiper(NUM_PIXELS, Pixel(0, 255, 0), 30),
            lambda: TheatreChaser(NUM_PIXELS, Pixel(127, 127, 127), 50),
            lambda: Rainbow(NUM_PIXELS),
            lambda: RainbowCycle(NUM_PIXELS)
        ]

    def generate(self):
        self.update_generator()
        return self.current_generator.generate()

    def update_generator(self):
        if time.time() - self.last_change_time > 2.0:
            self.current_generator = self.get_next_generator()
            self.last_change_time = time.time()

    def get_next_generator(self):
        self.generator_idx = (self.generator_idx + 1) % len(self.generators)
        return self.generators[self.generator_idx]()


class ColorWiper: # implements Generator
    def __init__(self, num_pixels, color, delay_ms):
        self.pixels = [Pixel() for i in range(num_pixels)]
        self.color = color
        self.delay_ms = delay_ms
        self.time_start = time.time()

    def generate(self):
        num_pix = self.num_pix_to_light()
        for i in range(num_pix):
            self.pixels[i].copy_colour(self.color)
        return self.pixels

    def num_pix_to_light(self):
        elapsed = time.time() - self.time_start
        return min(len(self.pixels), int ((elapsed * 1000) / self.delay_ms))


class TheatreChaser:
    def __init__(self, num_pixels, color, delay_ms):
        self.pixels = [Pixel() for i in range(num_pixels)]
        self.color = color
        self.delay_ms = delay_ms

    def generate(self):
        [p.clear() for p in self.pixels]
        offset = int(1000 * time.time()) % (self.delay_ms * 3) // self.delay_ms
        for i in range(0, len(self.pixels), 3):
            if i + offset >= len(self.pixels):
                continue
            self.pixels[i + offset].copy_colour(self.color)
        return self.pixels


class Rainbow:
    def __init__(self, num_pixels):
        self.pixels = [Pixel() for i in range(num_pixels)]
        self.time_start = 0

    def generate(self):
        uptime = time.time() - self.time_start
        col_offset = (int(uptime * 1000) % 5120) // 20
        for i in range(len(self.pixels)):
            self.pixels[i].copy_colour(_wheel(i + col_offset & 255))
        return self.pixels


class RainbowCycle:
    def __init__(self, num_pixels):
        self.pixels = [Pixel() for i in range(num_pixels)]
        self.time_start = 0

    def generate(self):
        uptime = time.time() - self.time_start
        col_offset = (int(uptime * 1000) % (5120 * 5)) // 100
        for i in range(len(self.pixels)):
            color = _wheel(int(((i * 256 / len(self.pixels)) + col_offset)) & 255)
            self.pixels[i].copy_colour(color)
        return self.pixels


def _wheel(pos):
    pos = 255 - pos
    if pos < 85:
        return Pixel(255 - pos * 3, 0, pos * 3)
    if pos < 170:
        pos -= 85
        return Pixel(0, pos * 3, 255 - pos * 3)
    pos -= 170
    return Pixel(pos * 3, 255 - pos * 3, 0)
