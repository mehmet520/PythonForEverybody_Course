#Using Python to Access Web Data
# Woche 4
# 12.5 - Parsing Web Pages
import urllib.request, urllib.parse, urllib.error 
from bs4 import BeautifulSoup

url= input ('Enter - URL\n')
print ('\nurl: ', url)
html= urllib.request.urlopen (url).read()
print ('\nhtml: ', html)
x=input ('\nDevam')

soup= BeautifulSoup(html, 'html.parser')
print('\nsoup :', soup)
x=input('Devam?')

# Retrieve all of the anchor tags
tags = soup ('a')
print('tags : ', tags)
z=input('Devam?')

for tag in tags:
    print (tag.get ('href', None))