"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
from FlaskWebProject1 import *
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

@app.route('/urlshortener', methods=['POST'])
def urlShortenerReturn():
    url = request.form['url']
    custom = request.form['custom']
    u = Url(url=url, shortenedUrl=custom)
    db.session.add(u)
    db.session.commit()
    return render_template(
        'urlReturn.html',
        title='Your New URL',
        year = datetime.now().year,
        url = urlGen(url, custom),
    )

@app.route('/manageUrls')
def manageUrls():
    dbCol = Url.query.all()
    return render_template(
        'manageUrls.html',
        title='Manage URLs',
        year = datetime.now().year,
        dbCol = dbCol,
    )