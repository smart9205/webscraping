import json
import requests
from flask import Flask, render_template, request


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time

import numpy as np
import cv2

app = Flask(__name__)

# base_url='https://scrapingclub.com'
base_url = 'https://www.twitch.tv'
duration=['24hr', '7d', '30d', 'all']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    output = request.get_json()
    result=json.loads(output)
    # url = base_url+'/'+result['name']+'/clips?filter=clips&range='+duration[int(result['topD'])-1]
    # url='https://scrapingclub.com/exercise/list_infinite_scroll/'

    url="https://www.twitch.tv/tarik/clips?filter=clips&range=7d"

    driver = webdriver.Chrome()
    driver.get(url)

    last_height = driver.execute_script('return document.body.scrollHeight')

    # while True:
    #     driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    #     time.sleep(2)
    #     new_hight = driver.execute_script('return document.body.scrollHeight')
    #     if(new_hight == last_height):
    #         break
    #     last_height = new_hight

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    

    # print(soup)

    # section = soup.find(class_='col-lg-8')
    # products = section.find_all(class_='col-lg-4 col-md-6 mb-4')

    # section = soup.find(class_='ScTower-sc-1dei8tr-0 dcmlaV tw-tower')
    products = soup.find_all('article')
    # print(products)

    
    cnt=0
    array=[]
    for element in products:
        # image_url = element.find('img', class_="card-img-top img-fluid")
        # imgurl=base_url+image_url['src']
        # href=element.find_all('a')[1]
        # href_url =base_url + href['href']
        # title=href.text
        # price = element.find('h5').text

        image_url=element.find_all(class_='tw-image')
        img1=image_url[0]['src']
        img2=image_url[1]['src']
        a_tag = element.find_all('a')
        href_url=base_url+a_tag[4]['href']

        # driver2 = webdriver.Chrome()
        # driver2.get(href_url)
        # last_height = driver2.execute_script('return document.body.scrollHeight')
        # soup2 = BeautifulSoup(driver2.page_source, 'html.parser')
        # products = soup2.find('video')
        # video_url = soup2.find('video')['src']

        

        ds = element.find_all(class_='ScMediaCardStatWrapper-sc-1ncw7wk-0 jluyAA tw-media-card-stat')
        dr = ds[0].text
        views = ds[1].text
        tm = ds[2].text

        title = element.find('h3').text
        name = a_tag[1].text
        desc = a_tag[2].text


        obj={
            "url":img2,
            "avatar":img1, 
            "href_url":href_url, 
            "duration":dr, 
            "views": views,
            "tm":tm,
            "title":title,
            "name":name,
            "desc":desc
        }  
        array.append(obj)
        cnt+=1

    json_array = json.dumps(array)
    # print(json_array)
    print(cnt)    
    return array


@app.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':
        configs = request.form['file_attach']
        # intro = configs['intro']
        print("-----------------")
        print(configs)
    return 1
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)