# Willkommen, Mehmet Yilmaz aus Using Python to Access Web Data
# Extracting Data from JSON
# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py.
# The program will prompt for a URL, read the JSON data from that URL using urllib and then parse
# and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing 
# and the other is the actual data you need to process for the assignment.
# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1258380.json (Sum ends with 62)
# You do not need to save these files to your folder since your program will read the data directly from the URL.

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