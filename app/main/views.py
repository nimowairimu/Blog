from flask import render_template,request
from app.main import main
from ..requests import get_quotes


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    quotes = get_quotes()
    return render_template('index.html',quote = quotes)
