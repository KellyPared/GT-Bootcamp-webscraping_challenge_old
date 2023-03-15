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


def lastest_news(browser):
    '''This function will scrape the web for featured titles and blurbs.'''
    browser.visit('https://static.bc-edx.com/data/web/mars_news/index.html')
    # assign URL
    url = "https://static.bc-edx.com/data/web/mars_news/index.html"
    browser.visit(url)
    #beautiful soup
    html_content = requests.get(url).text
    soup = bs4(html_content, "html.parser")
    mars_text = soup.find().text
    title_results = soup.find_all('div', class_ = 'content_title')
    description_results = soup.find_all('div', class_ = 'article_teaser_body')
    
    web_texts =[]
    titles = []
    descriptions = []

    for title in title_results:
        titles.append(title.text)
        for description in description_results:
            descriptions.append(description.text)
            web_text_dict = {
                "article_title":title.text,
                "article_teaser": description.text
            }
            web_texts.append(web_text_dict)
    
    return web_texts, titles, descriptions


def featured_mars(browser):
    '''This function will scrape the featured image and 
    pull the link to that image.'''

    # assign URL
    url_image = "https://spaceimages-mars.com/"
    browser.visit(url_image)
    my_service = Service()
    search_button = browser.find_by_xpath('//div[1]/div/a/button')
    search_button.click()
    time.sleep(2)
    image_tag = browser.find_by_xpath('/html/body/div[8]/div/div/div/div/img')
    featured_image_url = image_tag['src']
    return featured_image_url


def mars_table():
    url = 'https://galaxyfacts-mars.com/'
    all_tables = pd.read_html(url)
    mars_table = all_tables[0]
    scraped_table = mars_table.to_html(classes = 'table')
    return scraped_table


def hemispheres():
    url_hemis = 'https://marshemispheres.com/'
    html_content = requests.get(url_hemis).text
    soup = bs4(html_content, "html.parser")
    mars_image = soup.find().text
    # list_hemis = []
    # list_hemis.append({title: #text,
    #  img_url: #url
    #  })

    #return [#list of dictionaries]
    

def scrape():
    ''' This scrapes the page. main function'''
    browser = open_browser()
    web_texts, titles, descriptions = lastest_news(browser)
    image_url = featured_mars(browser)
    mars_tbl = mars_table()

    
    mars_dictionary = {'news_title': titles[0],
                       'news_paragraph': descriptions[0],
                       'featured_image': image_url,
                        'facts': mars_tbl,
                        'hemispheres': []
                       }

scrape()