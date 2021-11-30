from os import closerange
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

def find_desired_link (url):
    html = urllib.request.urlopen (url).read()
    soup = BeautifulSoup(html, 'html.parser')
    url_tag = soup('a')[17]
    name = url_tag.text
    url = url_tag.get('href')
    return url, name;

url= 'http://py4e-data.dr-chuck.net/known_by_Prabhjoit.html'

for i in range(7):
    url, name = find_desired_link (url)
print('\nName: ', name, '\nURL : ', url,'\n')