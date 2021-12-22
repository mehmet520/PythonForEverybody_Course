import urllib.parse, urllib.request, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url_adress= input ('\nEnter location (website URL) :')
# url_adress = 'http://py4e-data.dr-chuck.net/comments_42.json'
# url_adress = 'http://py4e-data.dr-chuck.net/comments_1258380.json'
print('Retrieving', url_adress)
url_connect = urllib.request.urlopen(url_adress, context = ctx)
# print('\nurl_connect :\n', url_connect)
url_data = url_connect.read().decode('utf-8')
# print('\nurl_data :\n', url_data)
print('Retrieved', len(url_data), 'characters')
try:
    js_data = json.loads(url_data)
except:
    js_data = None

comments = js_data["comments"]
# print ('\ncomments :\n', comments)
numbers = list()
for comment in comments:
    count = comment['count']
    numbers.append(count)
# print(numbers)
print('Count: ', len(numbers))
numbers_sum = sum(numbers)
print('Sum: ', numbers_sum)