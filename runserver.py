"""
This script runs the FlaskWebProject1 application using a development server.
"""

from os import environ
from FlaskWebProject1 import app
from flask import Flask, request
from flask_restful import Resource, Api
from flask import Response

import readHTMLPage
import readOasenHTMLPage
import time

app = Flask(__name__)
api = Api(app)

#Snäckviken starts here
class getMenuToday(Resource):
    def get(self):

        menu = readHTMLPage.getMenu()
        today = time.strftime("%A").lower()

        if(today == 'monday' or today == 'måndag'):
            return {'Monday': [menu[0], menu[1], menu[2], menu[3], menu[4], menu[5]]}

        if(today == 'tuesday' or today == 'tisdag'):
            return {'Tuesday': [menu[6], menu[7], menu[8], menu[9], menu[10], menu[11]]}

        if(today == 'wednesday' or today == 'onsdag'):
            return {'Wednesday': [menu[12], menu[13], menu[14], menu[15], menu[16], menu[17]]}

        if(today == 'thursday' or today == 'torsdag'):
            return {'Thursday': [menu[18], menu[19], menu[20], menu[21], menu[22], menu[23]]}

        if(today == 'friday' or today == 'fredag'):
            return {'Friday': [menu[24], menu[25], menu[26], menu[27], menu[28], menu[29]]}

class getMenu(Resource):
    def get(self):

        menu = readHTMLPage.getMenu()

        menuJson = {'Monday': [menu[0], menu[1], menu[2], menu[3], menu[4], menu[5]],
                    'Tuesday': [menu[6], menu[7], menu[8], menu[9], menu[10], menu[11]],
                    'Wednesday': [menu[12], menu[13], menu[14], menu[15], menu[16], menu[17]],
                    'Thursday': [menu[18], menu[19], menu[20], menu[21], menu[22], menu[23]],
                    'Friday': [menu[24], menu[25], menu[26], menu[27], menu[28], menu[29]]}
        return menuJson


class getMenuDay(Resource):
    def get(self, day):       
        
        menu = readHTMLPage.getMenu()
        day = day.lower()
        
        if day == 'monday' or day == 'måndag':
            return {'Monday': [menu[0], menu[1], menu[2], menu[3], menu[4], menu[5]]}

        elif day == 'tuesday' or day == 'tisdag':
            return {'Tuesday': [menu[6], menu[7], menu[8], menu[9], menu[10], menu[11]]}

        elif day == 'wednesday' or day == 'onsdag':
            return {'Wednesday': [menu[12], menu[13], menu[14], menu[15], menu[16], menu[17]]}

        elif day == 'thursday' or day == 'torsdag':
            return {'Thursday': [menu[18], menu[19], menu[20], menu[21], menu[22], menu[23]]}

        elif day == 'friday' or day == 'fredag':
            return {'Friday': [menu[24], menu[25], menu[26], menu[27], menu[28], menu[29]]}

        else: 
            return ({'Message':'Bad request syntax, enter a valid workday'}, 400)

#Oasen starts here
class getOasenMenuToday(Resource):
    def get(self):

        menu = readOasenHTMLPage.getMenu()
        today = time.strftime("%A").lower()

        if(today == 'monday' or today == 'måndag'):
            return {'Monday': [menu[0], menu[1], menu[2]]}

        if(today == 'tuesday' or today == 'tisdag'):
            return {'Tuesday': [menu[3], menu[4], menu[5]]}

        if(today == 'wednesday' or today == 'onsdag'):
            return {'Wednesday': [menu[6], menu[7], menu[8]]}

        if(today == 'thursday' or today == 'torsdag'):
            return {'Thursday': [menu[9], menu[10], menu[11]]}

        if(today == 'friday' or today == 'fredag'):
            return {'Friday': [menu[12], menu[13], menu[14]]}

class getOasenMenu(Resource):
    def get(self):

        menu = readOasenHTMLPage.getMenu()

        menuJson = {'Monday': [menu[0], menu[1], menu[2]],
                    'Tuesday': [menu[3], menu[4], menu[5]],
                    'Wednesday': [menu[6], menu[7], menu[8]],
                    'Thursday': [menu[9], menu[10], menu[11]],
                    'Friday': [menu[12], menu[13], menu[14]]}
        return menuJson

class getOasenMenuDay(Resource):
    def get(self, day):       
        
        menu = readOasenHTMLPage.getMenu()
        day = day.lower()
        
        if day == 'monday' or day == 'måndag':
            return {'Monday': [menu[0], menu[1], menu[2]]}

        elif day == 'tuesday' or day == 'tisdag':
            return {'Tuesday': [menu[3], menu[4], menu[5]]}

        elif day == 'wednesday' or day == 'onsdag':
            return {'Wednesday': [menu[6], menu[7], menu[8]]}

        elif day == 'thursday' or day == 'torsdag':
            return {'Thursday': [menu[9], menu[10], menu[11]]}

        elif day == 'friday' or day == 'fredag':
            return {'Friday': [menu[12], menu[13], menu[14]]}

        else: 
            return ({'Message':'Bad request syntax, enter a valid workday'}, 400)

api.add_resource(getMenu, '/menuSnackviken')
api.add_resource(getMenuDay, '/menuSnackviken/<day>')
api.add_resource(getMenuToday, '/menuSnackvikenToday')
api.add_resource(getOasenMenu, '/menuOasen')
api.add_resource(getOasenMenuDay, '/menuOasen/<day>')
api.add_resource(getOasenMenuToday, '/menuOasenToday')

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
