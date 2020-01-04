from flask import Flask
import time
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!\n'


@app.route('/sleep')
def sleep():
    time.sleep(10)
    return 'sleep 10s\n'


@app.route('/bbb')
def hello():
    return "hello world"


def cli():
    app.run(host='0.0.0.0', port='5000')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
