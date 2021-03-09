from flask import render_template
from .import main

@main.errorhandler(404)
def error_four_Ow_four(error):
    return render_template('fourOwfour.html'), 404