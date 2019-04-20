import argparse
import sys

sys.path.append('..')
from pixel_patterns.pixel_strip_patterns import BunchOfPatterns

DESCRIPTION = 'display demo patterns on various light devices'


def main():
    args = ArgParser(DESCRIPTION).parse_args()

    def create_displayer(generate_func):
        if args.device == 'pygame':
            print('using pygame to display pixels')
            from light_drivers.pygame_pixels.pygame_pixels import PygamePixelDisplayer
            return PygamePixelDisplayer(generate_func)
        elif args.device == 'arduino':
            print('using arduino to display pixels')
            from light_drivers.arduino_pixels.py_serial_pixels.serial_pixel_displayer import SerialPixelDisplayer
            return SerialPixelDisplayer(generate_func)
        elif args.device == 'phat':
            print('using unicorn pHAT to display pixels')
            from light_drivers.phat_pixels.phat_displayer import PhatDisplayer
            return PhatDisplayer(generate_func)
        else:
            raise Exception('unknown displayer: ' + args.device)

    print('press ctrl-c to exit')

    patterns = BunchOfPatterns()
    displayer = create_displayer(patterns.generate)
    try:
        displayer.run()
    finally:
        displayer.dispose()


class ArgParser:
    def __init__(self, description):
        self.description = description

    def parse_args(self):
        arg_parser = argparse.ArgumentParser(description=self.description)
        arg_parser.add_argument('--num_pixels', help='number of pixels on the device', type=int)
        arg_parser.add_argument('--device', help='set the display device (default: %(default)s)',
            choices=['pygame', 'arduino', 'phat'],
            default='pygame')
        return arg_parser.parse_args()


if __name__ == "__main__":
    main()
