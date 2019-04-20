import sys
sys.path.append('..')
from pixel_patterns.pixel_strip_patterns import BunchOfPatterns

USAGE = 'usage: python3 demo.py [pygame|arduino|phat]'


DISPLAYER = 'pygame'
if len(sys.argv) == 1:
    DISPLAYER = 'pygame'
elif len(sys.argv) == 2:
    DISPLAYER = sys.argv[1]
else:
    print(USAGE)


def create_displayer(generate_func):
    if DISPLAYER == 'pygame':
        print('using pygame to display pixels')
        from light_drivers.pygame_pixels.pygame_pixels import PygamePixelDisplayer
        return PygamePixelDisplayer(generate_func)
    elif DISPLAYER == 'arduino':
        print('using arduino to display pixels')
        from light_drivers.arduino_pixels.py_serial_pixels.serial_pixel_displayer import SerialPixelDisplayer
        return SerialPixelDisplayer(generate_func)
    elif DISPLAYER == 'phat':
        print('using unicorn pHAT to display pixels')
        from light_drivers.phat_pixels.phat_displayer import PhatDisplayer
        return PhatDisplayer(generate_func)
    else:
        raise Exception('unknown displayer: ' + DISPLAYER)

print('press any key to exit')

patterns = BunchOfPatterns()
displayer = create_displayer(patterns.generate)
try:
    displayer.run()
finally:
    displayer.dispose()
