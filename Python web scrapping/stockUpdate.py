import requests

import bs4

from bs4 import BeautifulSoup



def priceTracker():
    response = requests.get('https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch')

    soup=bs4.BeautifulSoup(response.text,'lxml')

    price = soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price
while True:
    #what ever priceTracker returns will be cast into a str and added to the print
    print('Current Amazon stock price is :' +str(priceTracker()))
