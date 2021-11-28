# import bs4 as b
import urllib.request, urllib.parse, urllib.error

from bs4 import BeautifulSoup
souce=urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup=BeautifulSoup (souce, 'lxml')
print()

# print(soup.find_all('p'))
# for paragraph in soup.find_all('p'):
#     print(paragraph.text)
# print (soup.get_text())
for url in soup.find_all('a'):
    print(url.get('href'))
print()
