from scrape_mars import scrape
from flask import Flask

app = Flask(__name__)


@app.route('/scrape')
def call_scrape():
    scrape()
    return #dictionary

@app.route('/')
def query_database():
    '''This function will query daatbase and pass mars data into HTML'''








