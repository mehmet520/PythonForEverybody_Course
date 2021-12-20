import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import ssl

# aapi_key = False
# # If you have a Google Places API key, enter it here
# # api_key = 'AIzaSy___IDByT70'
# # https://developers.google.com/maps/documentation/geocoding/intro

# if api_key is False:
#     api_key = 42
#     serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
# else :
#     serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input ('\nEnter URL :\n')
url=''
# if len(url)< 1: url= 'http://py4e-data.dr-chuck.net/comments_42.xml'
if len(url)< 1: url= 'http://py4e-data.dr-chuck.net/comments_1258379.xml'
# souce         :  <http.client.HTTPResponse object at 0x000002C37D393E20>
# Type of souce :  <class 'http.client.HTTPResponse'>
souce= urllib.request.urlopen (url)

# Type of souce_read : <class 'bytes'>
# with read method url data is read als bytes-b
souce_read = souce.read()   

# Type of souce_xml : <class 'str'>
# with decode methode from utf-8 to xml format
souce_xml= souce_read.decode('utf-8')   
# soup = BeautifulSoup (souce, 'lxml')
# print ('\nsoup: \n\n', soup)

souce_tree = ET.fromstring (souce_read) 
lst_comments = souce_tree.findall ('comments/comment')

# you can use an XPath selector string to look through the entire
# tree of XML for any tag named 'count' with the following line of code:
lst_all_count = souce_tree.findall ('.//count')
print ('\nTree of XML for count:\n', lst_all_count)

# print('\nType of souce : \n', type(souce))
# print('\nsouce: \n', souce)
# print ('\nRetrieved', len(souce_read), 'characters\n')

# x= input('\nfor souce_read continue?\n')
# print('\nType of souce_read: \n', type(souce_read))
# print ('\nsoup: \n\n', souce_read)

# x= input('\nfor souce_xml continue?\n')
# print('\nType of souce_xml: \n', type(souce_xml))
# print ('\nsoup_xml: \n\n', souce_xml)

# x= input('\nfor souce_tree continue?\n')
print('\nType of souce_tree: \n', type(souce_tree))
print ('\nsouce_tree: \n\n', souce_tree)
print('\nlst_comment: \n', lst_comments)

# Finding Names in URL, making list, count the names
# name_list= list ()
# count_name= {}
# for item in lst_comments:
#     name= item.find ('name').text
#     # name_list.append (name)
#     # count_name [name] = count_name.get ('name', 0)+ 1
   
# print ('\nName List: \n', name_list)
# print ('\nName Count List: \n', count_name)

# finding counts in URL, making list, count the counts and sum the numbers in counts
count_list = list ()
count_count = dict ()
for item in lst_comments:
    num_in_count = int ( item.find ('count').text)
    count_list.append (num_in_count)
    count_count [item.find ('count').text] = count_count.get (item.find ('count').text, 0) + 1

sum_of_count_list= sum (count_list)
print ( '\nsum_of_count_list :\n', sum_of_count_list)

print ('\nCount of Numbers:\n', count_count)