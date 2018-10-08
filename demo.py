from pixel_patterns.pixel_strip_patterns import BunchOfPatterns

DISPLAYER = 'pygame'
# DISPLAYER = 'arduino'

def create_displayer(generate_func):
    if DISPLAYER == 'pygame':
        print('using pygame to display pixels')
        from pygame_pixels.pygame_pixels import PygamePixelDisplayer
        return PygamePixelDisplayer(generate_func)
    elif DISPLAYER == 'arduino':
        print('using arduino to display pixels')
        from arduino_pixels.py_serial_pixels.serial_pixel_displayer import SerialPixelDisplayer
        return SerialPixelDisplayer(generate_func)

print('press any key to exit')

patterns = BunchOfPatterns()
displayer = create_displayer(patterns.generate)
try:
    displayer.run()
finally:
    displayer.dispose()
