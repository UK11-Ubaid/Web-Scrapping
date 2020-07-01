from lxml import html
import requests

URL = 'https://www.loans.co.za/compare-loans'
page = requests.get(URL)
tree = html.fromstring(page.content)

catchphrase = tree.xpath('//p[@class = "catchphrase"]/text()')
amount = tree.xpath('//span[@class = "amountRange"]/text()')
repPeriod = tree.xpath('//span[@class = "repaymentPeriod"]/text()')
#from line 11 to 14 will print each element and then go to next to print
#print(catchphrase)
#print(amount)
#print(repPeriod)

#line 16 to 25 will print info in a group
output = []
for info in zip(catchphrase,amount, repPeriod):
    resp = {}
    resp['catchphrase'] = info[0]
    resp['amount'] = info[1]
    resp['period'] = info[2]
    output.append(resp)

print(output)


