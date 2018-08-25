import pygame

BLACK = (0, 0, 0)
NUM_LEDS = 20
LED_HEIGHT = 20
LED_WIDTH = 20

pygame.init()
pygame.display.set_caption("pygame neopixels")
# window size = single LED height strip of NUM_LEDS
# note: minimum height seems to be ~50px
size = [LED_WIDTH * NUM_LEDS, LED_HEIGHT]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


def main():
    pixels = [Pixel(LED_HEIGHT, LED_WIDTH, i * LED_WIDTH, 0) for i in range(NUM_LEDS)]
    for i, p in enumerate(pixels):
        for j in range(i):
            incr_pixel(p)
            incr_pixel(p)
    done = False
    while not done:
        try:
            ms = clock.tick(50)
            screen.fill(BLACK)
            update_pixels(pixels, ms)
            for p in pixels:
                p.draw(pygame, screen)
            pygame.display.flip()
        except KeyboardInterrupt:
            done = True
    pygame.quit()

def update_pixels(pixels, ms):
    for p in pixels:
        incr_pixel(p)

def incr_pixel(pixel):
    for i in range(3):
        pixel.rgb[i] += 3
        if pixel.rgb[i] >= 256:
            pixel.rgb[i] = 0


class Pixel:
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
