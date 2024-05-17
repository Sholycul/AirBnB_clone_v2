#!/usr/bin/python3
""" This is our serviced homepage """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    This hello HBNB home page
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_page():
    """
    This page displays HBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_page(text):
    """
    This page displays C with some provided text
    """
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_page(text):
    """
    This page displays Python with some provided text
    If no text provided, it renders 'is cool'
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    Function that displays "n is a number" if n is an integer.
    """
    return '{:d} is a number'.format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
