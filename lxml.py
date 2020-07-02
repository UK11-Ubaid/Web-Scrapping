from lxml import html
import requests
import pandas as pd
import time
import lxml.html
from lxml import etree
import os
import urllib.parse 

URL = 'https://www.loans.co.za/compare-loans'
page = requests.get(URL)
tree = html.fromstring(page.content)

catchphrase = tree.xpath('//p[@class = "catchphrase"]/text()')
amount = tree.xpath('//span[@class = "amountRange"]/text()')
repPeriod = tree.xpath('//span[@class = "repaymentPeriod"]/text()')

session = requests.Session()
response = requests.get(URL, verify=False)
obj = lxml.html.document_fromstring(response.text)
obj = lxml.html.document_fromstring(response.text)
div = obj.xpath('/html/body/main/div/div/div[1]')[0]
p = div.getchildren()[4].getchildren()[0].getchildren()[-1]
links = obj.xpath('/html/body/main/div/div/div[1]/div[2]/article[*]/p[3]/a[1]')
links = [l.attrib['href'] for l in links]

r = session.get(links[0], verify = False)
absa = lxml.html.document_fromstring(r.text)
section = absa.xpath('/html/body/main/div/div/div[1]/section[2]')

print(section[0].getchildren()[1].text)

for i in links:
    url_parts = urllib.parse.urlparse(i)
    path_parts = url_parts[2].rpartition('/')[2]
    print(path_parts)
    #print('URL: {}\nreturns: {}\n'.format(i, path_parts[2]))
    
print("scrapping data from: https://www.loans.co.za/compare-loans")
time.sleep(2)

Supplier = []
CatchPhrase = []
Amount = []
Period = []
link = []
for info in zip(catchphrase, amount,repPeriod, links):
    CatchPhrase.append(info[0])
    Amount.append(info[1])
    Period.append(info[2])
    link.append(info[3])
    
df = pd.DataFrame({'Supplier': Supplier, 'Catchphrase': CatchPhrase, 'Amount': Amount, 'RepaymentPeriod': Period, 'Links': link})
df
