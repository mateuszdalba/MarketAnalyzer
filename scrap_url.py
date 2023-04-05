import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.olx.pl/d/oferta/mac-pro-6-1-3-5gghz-6-core-32gb-ram-dual-d500-1tb-ssd-CID99-IDTBW0f.html'

def scrap_from_url(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    #Scrap Category and Subcategory
    data_cat = []
    for offer in soup.find_all('div', {'class': 'css-6rrh1l'}):
        try:
            cat = offer.find('a', {'class': 'css-tyi2d1'})['href']
            data_cat.append(cat)
        except:
            pass
    
    #Main Scrap
    data_cat = []
    for offer in soup.find_all('div', {'class': 'css-1wws9er'}):
        pass

        # ##TODO
        # try:
        #     cat = offer.find('a', {'class': 'css-tyi2d1'})['href']
        #     data_cat.append(cat)
        # except:
        #     pass

