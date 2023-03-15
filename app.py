from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route('/')
def query_database():
    '''This function will query database and pass mars data into HTML'''

@app.route('/scrape')
def scrape():
    
    return #dictionary






