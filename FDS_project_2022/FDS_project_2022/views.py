"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
from FDS_project_2022 import app
from FDS_project_2022.repo.functions import *

@app.route('/')
@app.route('/home')
def home():
    print('Request for index page received')

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

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/predictemotion', methods=['GET', 'POST'])
def predictemotion():
    ret = "An error occurred"
    if request.method == 'POST':
        inputSentence = request.form['inputsentence']
        emotion = predictEmotion(inputSentence)
        if emotion == "positive":
            ret = "Positive emotion detected :)"
        elif emotion == "negative":
            ret = "Negative emotion detected :("
        elif emotion == "ambiguous":
            ret = "Ambiguous emotion detected :/"
                
    return render_template('index.html',
        title='Home Page',
        year=datetime.now().year,
        result=ret)