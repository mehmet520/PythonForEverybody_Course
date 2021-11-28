import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url_1='http://py4e-data.dr-chuck.net/comments_1258377.html'
html_1=urllib.request.urlopen(url_1).read()
soup_1=BeautifulSoup(html_1, 'html.parser')
numbers=list()
sumup=0
for tr in soup_1 ('span'):
    tr=tr.text
    numbers.append(int(tr))
for number in numbers:
    sumup=sumup+number
# print(numbers)
print(sumup)