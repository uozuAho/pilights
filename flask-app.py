import sys
import argparse

from flask import Flask, request
from py import neopixels

DESCRIPTION = """
Web server for remote control of neopixels.
"""

DEBUG = True
NUM_LEDS = 8

app = Flask(__name__, static_url_path='')
app.config.from_object(__name__)

pixels = neopixels.new_instance(NUM_LEDS)

def parse_args():
    arg_parser = argparse.ArgumentParser(description=DESCRIPTION)
    arg_parser.add_argument('--host', help='set the host address of the server, ' +
        'eg. 0.0.0.0 to accept external requests')
    return arg_parser.parse_args()

@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/setcolor', methods=['POST'])
def set_color():
    r = int(request.form['r'])
    g = int(request.form['g'])
    b = int(request.form['b'])
    pixels.set_all(r, g, b)
    return "OK"


if __name__ == '__main__':
    args = parse_args()
    host = args.host if args.host else None
    app.run(host)
