import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.olx.pl/d/oferta/mac-pro-6-1-3-5gghz-6-core-32gb-ram-dual-d500-1tb-ssd-CID99-IDTBW0f.html'

def scrap_from_url(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # #Scrap Category and Subcategory
    # data_cat = []
    # for offer in soup.find_all('div', {'class': 'css-6rrh1l'}):
    #     try:
    #         cat = offer.find('a', {'class': 'css-tyi2d1'})['href']
    #         data_cat.append(cat)
    #     except:
    #         pass
    
    #Find categories
    cats = soup.find_all('a', {'class': 'css-tyi2d1'})
    print(cats[-1])
    


    #Main Scrap
    data = []
    for offer in soup.find_all('div', {'class': 'css-1wws9er'}):
        try:
            title = offer.find('h1', {'class': 'css-lsoizd er34gjf0'}).text.strip()
            print(title)
            price = offer.find('h3', {'class': 'css-ddweki'}).text.strip()
            date = offer.find('span', {'class': 'css-l9yf5ek'}).text.strip()
            add = offer.find('p', {'class':'css-b5mlrv'}).text.strip()
            desc = offer.find('div', {'class':'css-bgzo2k'}).text.strip()
            views = offer.find('span', {'data-testid':'page-view-text'}).text.strip()

            #link = offer.find('a', {'class': 'css-rc5s2u'})['href']
            #loc_date = offer.find('p', {'class':'css-veheph er34gjf0'}).text.strip()

            

            data.append([title, price, date, add ,desc, views])
        except:
            pass



    #print(data_cat)
    print(data)

scrap_from_url(url)