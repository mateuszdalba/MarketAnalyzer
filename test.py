import requests
from bs4 import BeautifulSoup
import pandas as pd

#print(soup)
#css-1sw7q4x
#css-oukcj3


url = 'https://www.olx.pl/elektronika/'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')


data = []
for offer in soup.find_all('div', {'class': 'css-1sw7q4x'}):
    print(offer)
    print('\n')
    try:
        title = offer.find('h6', {'class': 'css-16v5mdi er34gjf0'}).text.strip()
        print(title)
        price = offer.find('p', {'data-testid': 'ad-price'}).text.strip()
        link = offer.find('a', {'class': 'css-rc5s2u'})['href']
        data.append([title, price, link])
    except:
        pass

df = pd.DataFrame(data, columns=['Title', 'Price', 'Link'])

print(df)

df.to_csv('elektronika.csv')
