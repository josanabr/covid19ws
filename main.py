#!/usr/bin/env python3
#
# Script tomado de https://flask.palletsprojects.com/en/1.1.x/quickstart/
#
# Author: John Sanabria - john.sanabria@correounivalle.edu.co
# Date: 2020-03-28
#
from flask import Flask
from flask_restplus import Api, Resource

flask_app = Flask(__name__)
app = Api(app = flask_app)

name_space = app.namespace('main', description='Main APIs')

@name_space.route("/")
class MainClass(Resource):
	def get(self):
		return {
			"status": "Got new data"
		}
	def post(self):
		return {
			"status": "Posted new data"
		}
