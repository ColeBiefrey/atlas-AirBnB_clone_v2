#!/usr/bin/python3
""" runs app using Flask """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ called function using pull route """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ called function using hbnb route """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ called function using text route """
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """ called function using python and text route """
    if text is not 'is cool':
        text = text.replace('_', ' ')
    return 'Python %s' % text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
