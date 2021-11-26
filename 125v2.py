import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url=input('Enter URL: ')
html=urllib.request.urlopen(url).urlread()

soup=BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags=soup('a')
for tag in tags:
    print(tag.get('href', None))


