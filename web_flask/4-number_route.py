#!/usr/bin/python3
"""
    Starts a Flask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbn():
    """
        Returns Hello HBNB!
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
        Returns HBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text_var(text):
    """
        Displays text variable passed in
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python/<text>', strict_slashes=False)
def text_var_python(text="is cool"):
    """
        Displays text variable, with default "is cool"
    """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def var_num(n):
        """
             Displays a variable, but only if an int
        """
        return "{} is a number".format(n)
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
