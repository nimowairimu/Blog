from app import app
import urllib.request,json
from .models import quote
from app import app
import urllib.request,json


Quote = quote.Quote

# Getting api key
api_key = app.config['QUOTE_API_KEY']

# Getting the movie base url
base_url = app.config[" QUOTE_API_BASE_URL"]


def get_quotes():
    get_movies_url = base_url.format(api_key)
    response = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    if response.status_code == 200:
        quote = response.json()
        return quote

# import urllib.request,json
# from .models import Movie

# # Getting api key
# api_key = None
# # Getting the movie base url
# base_url = None

# def configure_request(app):
#     global api_key,base_url
#     api_key = app.config['MOVIE_API_KEY']
#     base_url = app.config['MOVIE_API_BASE_URL']
