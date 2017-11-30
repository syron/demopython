"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

# @app.route('/currencies')
# def currencies():
#     parser = reqparse.RequestParser()
#     parser.add_argument('base',required=False)
#     args = parser.parse_args()
#     URL = 'https://api.fixer.io/latest'

#     if args['base'] is None : parser.remove_argument('base')
#     elif args['base'] is not None : URL = 'https://api.fixer.io/latest?base='+args['base']
    
#     r = requests.get(URL, headers=None, data=None, verify=False)
#     return (r.json())

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
