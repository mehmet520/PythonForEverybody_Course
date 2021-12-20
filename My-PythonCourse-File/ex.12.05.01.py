#Using Python to Access Web Data
# Woche 4
# 12.5 - Parsing Web Pages
import urllib.request, urllib.parse, urllib.error 
from bs4 import BeautifulSoup

url= input ('Enter - URL\n')
if len(url)<1: url='https://pythonprogramming.net/parsememcparseface/'
print ('\nurl: \n', url)
html= urllib.request.urlopen (url).read()
print ('\nhtml: \n', html)
x=input ('\nDevam -1 soup : \n')

soup= BeautifulSoup(html, 'html.parser')
print('\nsoup :\n', soup)
x=input('\nDevam? - 2  tags  :\n')

# Retrieve all of the anchor tags
tags = soup ('a')
print('\ntags : \n', tags)
z=input('\nDevam? - 3 Tag <a> :   \n')

for tag in tags:
    print (tag)
z=input('\nDevam? - 4 href :   \n')
for tag in tags:
    print (tag.get ('href', None))