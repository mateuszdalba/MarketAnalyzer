import requests
from bs4 import BeautifulSoup
import pandas as pd

####################
### OLX.PL SCRAPPER
####################


#Sorting options:
### FROM LOWEST PRICE: ?search%5Border%5D=filter_float_price:asc
### FROM HIGHEST PRICE: ?search%5Border%5D=filter_float_price:desc
### FROM NEWEST: ?search%5Border%5D=created_at:desc
### MOST RELEVANT: ?search%5Border%5D=relevance:desc

# ?search%5Border%5D=filter_float_price:asc

#url_in = f'https://www.olx.pl/{category}/{sorting}'

def scrap_base(category,pages,sorting, subcategory = None, subcategory2 = None) -> pd.DataFrame():
    
    dfs_list = []

    for page in list(range(1, pages+1)):

        pgs = f'?page={page}'
        
        if subcategory == None:
            url = f'https://www.olx.pl/{category}/{pgs}&{sorting}'
        elif (subcategory is not None) and (subcategory2 is None) :
            url = f'https://www.olx.pl/{category}/{subcategory}/{pgs}&{sorting}'
        elif (subcategory is not None) and (subcategory2 is not None):
            url = f'https://www.olx.pl/{category}/{subcategory}/{subcategory2}/{pgs}&{sorting}'

        print(url)

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        data = []
        for offer in soup.find_all('div', {'class': 'css-1sw7q4x'}):
            #print(offer)
            #print('\n')
            try:
                title = offer.find('h6', {'class': 'css-16v5mdi er34gjf0'}).text.strip()
                price = offer.find('p', {'data-testid': 'ad-price'}).text.strip()
                link = offer.find('a', {'class': 'css-rc5s2u'})['href']
                status = offer.find('span', {'class': 'css-3lkihg'}).text.strip()
                loc_date = offer.find('p', {'class':'css-veheph er34gjf0'}).text.strip()

                data.append([title, price, link, status, loc_date])
            except:
                pass
        
        df = pd.DataFrame(data, columns=['Title', 'Price', 'Link', 'Status', 'Loc_Date'])
        dfs_list.append(df)

    
    rez = pd.concat(dfs_list)

    rez.to_csv('elektronika.csv', index=False)

    return rez



category = 'elektronika'
sorting = """search%5Border%5D=created_at:desc"""
pages = 15
subcategory = 'komputery'
subcategory2 = 'komputery-stacjonarne'


scrap_base(category, pages, sorting, subcategory, subcategory2)




