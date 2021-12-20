import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx= ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode= ssl.CERT_NONE

# url=input('\nEnter URL : \n')
# if len(url) <1:
url='https://pythonprogramming.net/parsememcparseface/'
print(url)
htmlraw=urllib.request.urlopen(url, context=ctx).read()
print(htmlraw)
# print('\nhtml Byte String: \n', htmlraw)
soup=BeautifulSoup(htmlraw, 'html.parser')
# print('\nsoup html tree : \n', soup)

# Retrieve all of the anchor tags
tags=soup('a')
# for tag in tags:
#     print ()
    # print (tag.get('href', None))
# print(tags)
# print( soup('head'))