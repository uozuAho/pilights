import argparse
from flask import Flask, request
import sys
from threading import Thread

sys.path.append('..')

from pixel_generator_slave import PixelGeneratorSlave


DESCRIPTION = """
Web server for remote control of neopixels.
"""

NUM_PIXELS = 43

app = Flask(__name__, static_url_path='')
app.config.from_object(__name__)
pixelgen = PixelGeneratorSlave(NUM_PIXELS)


@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/alloff', methods=['POST'])
def all_off():
    set_all_rgb(0, 0, 0)
    return "OK"

@app.route('/setall', methods=['POST'])
def set_all():
    color = request.args.get('color')
    if color == 'red':
        set_all_rgb(200, 0, 0)
    else:
        r = request.args.get('r') or 0
        g = request.args.get('g') or 0
        b = request.args.get('b') or 0
        set_all_rgb(int(r), int(g), int(b))
    return "OK"

def set_all_rgb(r, g, b):
    pixelgen.set_all(r, g, b)

def parse_args():
    arg_parser = argparse.ArgumentParser(description=DESCRIPTION)
    arg_parser.add_argument('--host', help='set the host address of the server, ' +
        'eg. 0.0.0.0 to accept external requests')
    arg_parser.add_argument('--device', help='set the display device (default: %(default)s)',
        choices=['pygame', 'arduino'],
        default='pygame')
    return arg_parser.parse_args()

def start_displayer(device):
    if device == 'pygame':
        from pygame_pixels.pygame_pixels import PygamePixelDisplayer
        pixeldisp = PygamePixelDisplayer(pixelgen.generate)
    elif device == 'arduino':
        from arduino_pixels.py_serial_pixels.serial_pixel_displayer import SerialPixelDisplayer
        pixeldisp = SerialPixelDisplayer(pixelgen.generate)
    else:
        raise Exception('unknown displayer device: ' + device)

    # run the displayer in a background thread, since it runs a blocking loop
    dispthread = Thread(target=pixeldisp.run)
    dispthread.start()

if __name__ == '__main__':
    args = parse_args()
    host = args.host if args.host else None
    start_displayer(args.device)
    app.run(host)
