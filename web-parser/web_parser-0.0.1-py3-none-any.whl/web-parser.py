import requests
from bs4 import BeautifulSoup as bs

def pub_text_parse(url, htmlel1, htmlel2):
	all_data = []
	r = requests.get(url)
	html = bs(r.content, 'html.parser')

	for el in html.select(htmlel1):
		data = el.select(htmlel2)
		all_data.append(data[0].text)
	return all_data