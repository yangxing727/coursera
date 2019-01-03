from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import os
def soup(url):
    print(url)
    content = urlopen(url).read()
    tmp = BeautifulSoup(content)
    return tmp