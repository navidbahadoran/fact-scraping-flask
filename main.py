#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests

response = requests.get('http://unkno.com/').content
soup = BeautifulSoup(response, 'lxml')
quotes = soup.find_all('div', id='content')[0].text.strip()
print(quotes)

