from lxml import html
import requests

URL = 'https://www.loans.co.za/compare-loans'
page = requests.get(URL)
tree = html.fromstring(page.content)

catchphrase = tree.xpath('//p[@class = "catchphrase"]/text()')
amount = tree.xpath('//span[@class = "amountRange"]/text()')
repPeriod = tree.xpath('//span[@class = "repaymentPeriod"]/text()')
print(catchphrase)
print(amount)
print(repPeriod)


