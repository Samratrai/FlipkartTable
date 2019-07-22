# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 14:44:38 2019

@author: dell
"""
import requests
import pandas as pd
from bs4 import BeautifulSoup

driver = requests.get('https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2').text
driver_soup = BeautifulSoup(driver,'html.parser')
#print(driver_soup)

products = []
prices = []
ratings = []
for a in driver_soup.find_all('a',href = True ,attrs= {'class': '_31qSD5'}):
    name = a.find('div', attrs = {'class' : '_3wU53n'})
    price = a.find('div', attrs = {'class' : '_1vC4OE _2rQ-NK'})
    rating = a.find('div', attrs = {'class' : 'hGSR34'})                                          
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)
#print(products)    
#print(prices)
#print(ratings)
df = pd.DataFrame({'Product Name': products, 'Price': prices, 'Rating': ratings})
print(df)