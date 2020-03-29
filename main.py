#!/usr/bin/env python3
#
# Script tomado de https://flask.palletsprojects.com/en/1.1.x/quickstart/
#
# Author: John Sanabria - john.sanabria@correounivalle.edu.co
# Date: 2020-03-28
#
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
