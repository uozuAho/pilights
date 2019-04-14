import pygame
import sys

sys.path.append('..')

from presenter import Pixel


BLACK = (0, 0, 0)
LED_HEIGHT = 50
LED_WIDTH = 20


class PygamePixelDisplayer:
    """ Implements the displayer interface for the pixel presenter """
    def __init__(self, generate_pixels):
        pygame.display.set_caption("pygame neopixels")
        pixels = generate_pixels()
        self.pixels = [_PygamePixel(LED_HEIGHT, LED_WIDTH, i * LED_WIDTH, 0) for i in range(len(pixels))]
        size = [LED_WIDTH * len(pixels), LED_HEIGHT]
        self.generate_pixels = generate_pixels
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()

    def __enter__(self):
        pygame.init()
        return self

    def __exit__(self, type, val, trace):
        pygame.quit()

    def dispose(self):
        pygame.quit()

    def set_generate_pixels(self, generate):
        self.generate_pixels = generate

    def run(self):
        done = False
        while not done:
            ms = self.clock.tick(50)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        print('escape pressed. quitting...')
                        done = True
            for pgpixel, pixel in zip(self.pixels, self.generate_pixels()):
                pgpixel.rgb = pixel.rgb
            self.render(self.pixels)

    def render(self, pixels):
        self.screen.fill(BLACK)
        for p in pixels:
            p.draw(pygame, self.screen)
        pygame.display.flip()


class _PygamePixel:
    """ Pygame-aware pixel that can draw itself """
    def __init__(self, height, width, left, top):
        self.height = height
        self.width = width
        self.left = left
        self.top = top
        self.rgb = [0, 0, 0]

    def draw(self, pg, screen):
        pygame.draw.rect(screen, self.rgb, [self.left, self.top, self.width, self.height])
