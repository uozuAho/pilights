from pixel_patterns.pixel_strip_patterns import BunchOfPatterns

# DISPLAYER = 'pygame'
DISPLAYER = 'arduino'

def create_displayer(generate_func):
    if DISPLAYER == 'pygame':
        print('using pygame to display pixels')
        from pygame_pixels.pygame_pixels import create_displayer
        raise 'uhh how to return a context managed thing?'
    elif DISPLAYER == 'arduino':
        print('using arduino to display pixels')
        from arduino_pixels.py_serial_pixels.main import SerialPixelDisplayer
        return SerialPixelDisplayer(generate_func)

print('press any key to exit')

patterns = BunchOfPatterns()
displayer = create_displayer(patterns.generate)
displayer.run()
