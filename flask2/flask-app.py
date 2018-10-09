import argparse
from flask import Flask, request
import sys
from threading import Thread

sys.path.append('..')

from pixel_generator_slave import PixelGeneratorSlave
from pygame_pixels.pygame_pixels import PygamePixelDisplayer

DESCRIPTION = """
Web server for remote control of neopixels.
"""

NUM_PIXELS = 43
DISPLAYER = 'pygame'
# DISPLAYER = 'arduino'

app = Flask(__name__, static_url_path='')
app.config.from_object(__name__)
pixelgen = PixelGeneratorSlave(NUM_PIXELS)
if DISPLAYER == 'pygame':
    pixeldisp = PygamePixelDisplayer(pixelgen.generate)
elif DISPLAYER == 'arduino':
    raise Exception('not implemented')

# run the displayer in a background thread, since it runs a blocking loop
dispthread = Thread(target=pixeldisp.run)
dispthread.start()


def parse_args():
    arg_parser = argparse.ArgumentParser(description=DESCRIPTION)
    arg_parser.add_argument('--host', help='set the host address of the server, ' +
        'eg. 0.0.0.0 to accept external requests')
    return arg_parser.parse_args()

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
        r = request.args.get('r')
        g = request.args.get('g')
        b = request.args.get('b')
        set_all_rgb(r, g, b)
    return "OK"

def set_all_rgb(r, g, b):
    pixelgen.set_all(r, g, b)


if __name__ == '__main__':
    args = parse_args()
    host = args.host if args.host else None
    app.run(host)
