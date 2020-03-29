#!/usr/bin/env python3
#
# Script tomado de https://flask.palletsprojects.com/en/1.1.x/quickstart/
#
# Author: John Sanabria - john.sanabria@correounivalle.edu.co
# Date: 2020-03-28
#
from flask import Flask, request
from flask_restplus import Api, Resource, fields
from time import gmtime, strftime
import constant # constantes de este proyecto
import fields # campos monitoreados
import time
import subprocess

flask_app = Flask(__name__)
app = Api(app = flask_app, version = "0.0.1", title = "COVID 19 Web Service", description = "Endpoint para consultar el avance del COVID 19 por pais" )

name_space = app.namespace('COVID19', description='Web Service COVID19')
model = app.model('Name Model', 
                  {'name': fields.String(required = True, 
                                         description="Name of the country", 
                                         help="Name cannot be blank.")
                  })

def findCountryData(country):
	cmd =  "grep %s %s/%s | tail -n 1"%(country,constant.COVIDDIR,constant.FILENAME)
	output = subprocess.check_output(cmd, shell = True)[:-1]
	print("[%s]"%(output))
	output = output.decode().split(',')
	if len(output) < 2:
		return { "Status": "%s Not Found"%(country) }
	dictio = {}
	dictio['GMT time'] = time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())
	dictio['Server time'] = strftime("%a, %d %b %Y %I:%M:%S %p %Z")
	dictio[fields.STDATETIME] = output[fields.DATETIME]
	dictio[fields.STCOUNTRY] = output[fields.COUNTRY]
	dictio[fields.STTCASES] = output[fields.TCASES]
	dictio[fields.STNCASES] = output[fields.NCASES]
	dictio[fields.STTDEATHS] = output[fields.TDEATHS]
	dictio[fields.STNDEATHS] = output[fields.NDEATHS]
	dictio[fields.STTRECOVERED] = output[fields.TRECOVERED]
	dictio[fields.STACASES] = output[fields.ACASES]
	dictio[fields.STSCRITICAL] = output[fields.SCRITICAL]
	dictio[fields.STCASEXMILLION] = output[fields.CASEXMILLION]
	dictio[fields.STDEATHSXMILLION] = output[fields.DEATHSXMILLION]
	dictio[fields.STFSTCASE] = output[fields.FSTCASE]

	return dictio

@name_space.route("/<string:id>")
class MainClass(Resource):
	@app.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'}, params={'id': 'Country'})
	def get(self,id = 'Colombia'):
		return findCountryData(id)
	@app.expect(model)
	def post(self):
		countryName = request.json['name']
		return findCountryData(countryName)
