"""
This script runs the FlaskWebProject1 application using a development server.
"""

from os import environ
from FlaskWebProject1 import app
from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful import reqparse
from flask import Response
import requests

app = Flask(__name__)
api = Api(app)

class getLatestCurrencies(Resource):
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('base',required=False)
        args = parser.parse_args()
        URL = 'https://api.fixer.io/latest'

        if args['base'] is None : parser.remove_argument('base')
        elif args['base'] is not None : URL = 'https://api.fixer.io/latest?base='+args['base']
        
        r = requests.get(URL, headers=None, data=None, verify=False)
        return (r.json())
        
class getConvertCurrency(Resource):
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('base',required=True)
        parser.add_argument('to',required=True)

        args = parser.parse_args()

        URL = 'https://api.fixer.io/latest?'+'base='+args['base']+'&'+'symbols='+args['to']

        r = requests.get(URL, headers=None, data=None, verify=False)
        return (r.json())

api.add_resource(getLatestCurrencies, '/latestCurrencies')
api.add_resource(getConvertCurrency, '/specificCurrency')


if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
