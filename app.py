from flask import Flask, request

DEBUG = True

app = Flask(__name__, static_folder='app', static_url_path='')
app.config.from_object(__name__)


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/setcolor', methods=['POST'])
def set_color():
    r = request.form['r']
    g = request.form['g']
    b = request.form['b']
    print(r, g, b)
    return "OK"


if __name__ == '__main__':
    app.run()
