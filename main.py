import requests as req
from bs4 import BeautifulSoup as BS

# some strings need to modify for working
r = req.get('site')
html = BS(r.content, 'html.parser')
for el in html.select('span.lem'):
	title = el.select('.css-16v5mdi.er34gjf0')
	price = el.select('p')
	link ='site' + el.find('a').get('href')
	if int(''.join(price[0].text.split()[:-1])) < 2000:
		print(title[0].text, price[0].text, link)

