#!/usr/bin/env python
from flask import Flask
from bs4 import BeautifulSoup
import requests
import os

app = Flask(__name__)


def get_fact():
    response = requests.get('http://unkno.com/').content
    soup = BeautifulSoup(response, 'lxml')
    quote = soup.find_all('div', id='content')[0].text.strip()
    return quote


@app.route('/')
def home():
    return get_fact()


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
