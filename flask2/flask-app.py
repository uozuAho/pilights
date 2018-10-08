import sys
import argparse

sys.path.append('..')

from flask import Flask, request
# from pi_pixels import neopixels

DESCRIPTION = """
Web server for remote control of neopixels.
"""

DEBUG = True
NUM_LEDS = 8

app = Flask(__name__, static_url_path='')
app.config.from_object(__name__)


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
    return "OK"

@app.route('/setall', methods=['POST'])
def set_all():
    color = request.args.get('color')
    print('color: ' + color)
    return "OK"


if __name__ == '__main__':
    args = parse_args()
    host = args.host if args.host else None
    app.run(host)
