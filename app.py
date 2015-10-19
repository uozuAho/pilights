from flask import Flask

DEBUG = True

app = Flask(__name__, static_folder='app', static_url_path='')
app.config.from_object(__name__)


@app.route('/')
def root():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run()
