from arg_parser import ArgParser
from flask import Flask, request

from pixel_service import PixelService


DESCRIPTION = """
Web server for remote control of neopixels.
"""

NUM_PIXELS = 43


app = Flask(__name__, static_url_path='')
app.config.from_object(__name__)
pixelservice = None


@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/alloff', methods=['POST'])
def all_off():
    pixelservice.set_all(0, 0, 0)
    return "OK"

@app.route('/setall', methods=['POST'])
def set_all():
    color = request.args.get('color')
    if color == 'red':
        pixelservice.set_all(200, 0, 0)
    else:
        r = request.args.get('r') or 0
        g = request.args.get('g') or 0
        b = request.args.get('b') or 0
        pixelservice.set_all(int(r), int(g), int(b))
    return "OK"

@app.route('/setpattern', methods=['POST'])
def set_pattern():
    name = request.args.get('name')
    if not name:
        return 'invalid pattern name', 400
    pixelservice.set_pattern(name)
    return "OK"


if __name__ == '__main__':
    args = ArgParser(DESCRIPTION).parse_args()
    host = args.host if args.host else None
    pixelservice = PixelService(NUM_PIXELS)
    pixelservice.start_displayer(args.device)
    app.run(host)
