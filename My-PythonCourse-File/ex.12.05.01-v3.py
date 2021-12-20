import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
sauce=urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup=BeautifulSoup(sauce, 'html.parser')
# for url in soup.find_all('a'):

nav=soup.nav
# for url in nav.find_all('a'):
#     print(url.get('href'))
   
# body=soup.body
# for paragraph in body.find_all('p'):
#     print(paragraph.text)

# for div in soup.find_all('div', class_='body'):
#     print(div.text)
for paragraph in soup.find_all('p'):
    # print('1. paragraph.string, '\n')
    # print (str(paragraph.text))
    print (paragraph.text)

# title of the page
print(soup.title)

# get attributes:
print(soup.title.name)

# get values:
print(soup.title.string)

# beginning navigation:
print(soup.title.parent.name)

# getting specific values:
print(soup.p)