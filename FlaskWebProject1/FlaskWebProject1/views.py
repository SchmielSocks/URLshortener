"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app
from FlaskWebProject1.urlGen import *

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Playground Hub',
        year=datetime.now().year,
    )

@app.route('/sample')
def sample():
    """Renders sample page."""
    return render_template(
        'sample.html',
        title='Sample Project Page',
        year=datetime.now().year,
    )

@app.route('/urlshortener')
def urlShortener():
    """Renders page that shortens URLs"""
    return render_template(
        'urlShortener.html',
        title='URL Shortener',
        year=datetime.now().year,
    )
