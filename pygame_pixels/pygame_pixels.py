from contextlib import contextmanager
import pygame
import sys

sys.path.append('..')

from presenter import Pixel


BLACK = (0, 0, 0)
LED_HEIGHT = 50
LED_WIDTH = 20


def main():
    gen = SimpleScrollGenerator(30)
    with create_displayer(gen.generate) as disp:
        disp.run()


class SimpleScrollGenerator:
    """ Generate a simple scrolling pattern for testing. Implements presenter.Generator """

    def __init__(self, num_pixels):
        self.pixels = [Pixel() for i in range(num_pixels)]
        for i, p in enumerate(self.pixels):
            for j in range(i):
                self.incr_pixel(p)
                self.incr_pixel(p)

    def generate(self, time):
        for p in self.pixels:
            self.incr_pixel(p)
        return self.pixels

    def incr_pixel(self, pixel):
        for i in range(3):
            pixel.rgb[i] += 3
            if pixel.rgb[i] >= 256:
                pixel.rgb[i] = 0


class PygamePixelDisplayer:
    """ Implements the displayer interface for the pixel presenter """
    def __init__(self, generate_pixels):
        pixels = generate_pixels()
        self.pixels = [PygamePixel(LED_HEIGHT, LED_WIDTH, i * LED_WIDTH, 0) for i in range(len(pixels))]
        size = [LED_WIDTH * len(pixels), LED_HEIGHT]
        self.generate_pixels = generate_pixels
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()

    def set_generate_pixels(self, generate):
        self.generate_pixels = generate

    def run(self):
        while True:
            ms = self.clock.tick(50)
            for pgpixel, pixel in zip(self.pixels, self.generate_pixels()):
                pgpixel.rgb = pixel.rgb
            self.render(self.pixels)

    def render(self, pixels):
        self.screen.fill(BLACK)
        for p in pixels:
            p.draw(pygame, self.screen)
        pygame.display.flip()


@contextmanager
def create_displayer(generate):
    """ Create a managed displayer instance, ensuring pygame.quit is called
        on error / exit
    """
    try:
        pygame.init()
        pygame.display.set_caption("pygame neopixels")
        yield PygamePixelDisplayer(generate)
    except:
        pygame.quit()
        raise
    else:
        pygame.quit()


class PygamePixel:
    """ Pygame-aware pixel that can draw itself """
    def __init__(self, height, width, left, top):
        self.height = height
        self.width = width
        self.left = left
        self.top = top
        self.rgb = [0, 0, 0]

    def draw(self, pg, screen):
        pygame.draw.rect(screen, self.rgb, [self.left, self.top, self.width, self.height])


if __name__ == '__main__':
    main()
