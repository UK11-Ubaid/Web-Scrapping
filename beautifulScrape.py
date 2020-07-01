import requests #to interact with html
from bs4 import BeautifulSoup #for beautifulsoup4
#from line 6 to 7
#This code performs an HTTP request to the given URL. It retrieves the HTML data that the server sends back and stores that data in a Python object.
URL = 'https://www.loans.co.za/compare-loans'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser') # creating beautifulsoup object and takes scrapped HTML content as its input

result = soup.find(id = 'content')


#grid-container div only prints the very first one 

loan = result.find_all('div', class_='tilesWrapper clearfix')


for a in loan:
        catchphrase = a.find('p', class_ = 'catchphrase')
        amount = a.find('span', class_='amountRange')
        repPeriod = a.find('span', class_ = 'repaymentPeriod')
        if None in(catchphrase, amount, repPeriod):
            continue
        print(catchphrase.text.strip())
        print(amount.text.strip())
        print(repPeriod.text.strip())
        print()
