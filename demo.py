from pixel_patterns.pixel_strip_patterns import BunchOfPatterns
from pygame_pixels.pygame_pixels import create_displayer

print('running neopixel pattern demo using pygame')
print('press any key to exit')

patterns = BunchOfPatterns()
with create_displayer(patterns.generate) as displayer:
    displayer.run()
