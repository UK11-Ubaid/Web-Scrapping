#imports
from lxml import html
import requests
import pandas as pd
import time
import lxml.html
import urllib.parse 

print("scrapping data from: https://www.loans.co.za/compare-loans...")
time.sleep(2)

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

r = session.get(links[11])
absa = lxml.html.document_fromstring(r.text)  
section = absa.xpath('/html/body/main/div/div/div[1]/section[2]')
paragraphs = section[0].getchildren()
sec = paragraphs[-1].getchildren() 
  
    
print("Getting suppliers info...")
time.sleep(1)
supplier = []
for i in links:
    url_parts = urllib.parse.urlparse(i)
    path_parts = url_parts[2].rpartition('/')[2]
    supplier.append(path_parts)

print("Getting catchphrase...")   
time.sleep(1)
print("Getting amount...")
time.sleep(1)
print("Getting repayment period...")
time.sleep(1)

print("Getting products offered...")
time.sleep(1)
lnk = len(links)
offer = []
for l in range(lnk):
        r = session.get(links[l])
        banks = lxml.html.document_fromstring(r.text)  
        section = banks.xpath('/html/body/main/div/div/div[1]/section[2]')
        paragraphs = section[0].getchildren()
        sec = paragraphs[-1].getchildren() 
        bs = []
        for value in sec:
            bs.append(value.text)
        offer.append(', '.join(bs))
      
print("Getting links...")
time.sleep(1)

print("Creating a table...")
time.sleep(2)
Supplier = []
CatchPhrase = []
Amount = []
Period = []
Product = []
Link = []
for info in zip(supplier,catchphrase, amount,repPeriod, offer, links):
    Supplier.append(info[0])
    CatchPhrase.append(info[1])
    Amount.append(info[2])
    Period.append(info[3])
    Product.append(info[4])
    Link.append(info[5])
     
    
df = pd.DataFrame({'Supplier': Supplier, 'Catchphrase': CatchPhrase, 'Amount': Amount, 'RepaymentPeriod': Period, 'Products Offered': offer, 'Links': Link})
df
