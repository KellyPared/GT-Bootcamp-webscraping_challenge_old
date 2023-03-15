# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as bs4
import requests
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint 
import csv
import os
import sys
import time
os.path.dirname(sys.executable)

def open_browser():
    '''This launches browser.'''
    #browser = webdriver.Chrome()
    #global browser
    browser = Browser('chrome')
    return browser

def lastest_news():
    
    return title, paragraph


def featured_mars():
    return url


def mars_table():
    url = 'https://galaxyfacts-mars.com/'
    all_tables = pd.read_html(url)
    tb = mars_table.to_html(classes = 'table')
    return tb

def hemispheres():
    list_hemis = []
    list_hemis.append({title: #text,
     img_url: #url
     })

    return [#list of dictionaries]

def scrape():
    ''' This scrapes the page. main function'''
    browser = open_browser()
    title, paragraph = lastest_news()
    image_url = featured_mars()

    
    mars_dictionary = {'news_title': title,
                       'news_paragraph': paragraph,
                       'featured_image': image_url,
                        'facts': mars_table(),
                        'hemispheres': []
                       }
