"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
from FDS_project_2022 import app
from FDS_project_2022.repo.functions import *
import html

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

@app.route('/predictemotion', methods=['GET', 'POST'])
def predictemotion():
    ret = "An error occurred"
    if request.method == 'POST':
        inputSentence = request.form['inputsentence']
        emotion = predictEmotion(inputSentence)
        if emotion == "positive":
            ret = "Positive emotion detected "+ html.unescape("&#x1F60A")
        elif emotion == "negative":
            ret = "Negative emotion detected "+ html.unescape("&#x1F623")
                
    return render_template('index.html',
        title='Home Page',
        year=datetime.now().year,
        result=ret,
        pictures= emotion,
        sentence=request.form['inputsentence'])