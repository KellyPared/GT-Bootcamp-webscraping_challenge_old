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

def scrape():
    ''' This scrapes the page.'''
    browser = open_browser()