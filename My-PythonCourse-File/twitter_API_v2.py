
# For sending GET requests from the API
import requests
#Environment variables are implemented through the os package, specifically os.environ
# For saving access tokens and for file management when creating and adding to the dataset
import os
# For dealing with json responses we receive from the API
import json
# For displaying the data after
import pandas as pd
# For saving the response data in CSV format
import csv
# For parsing the dates received from twitter in readable formats
import datetime
import dateutil.parser
import unicodedata
#To add wait time between requests
import time

# !doesn"t work to use environment variables in python
# from dotenv import load_dotenv, find_dotenv
# load_dotenv(find_dotenv())
# print('\nstripe .env file: ', os.getenv('costomer_key'))

# Environment Variables .env with Python: https://www.youtube.com/watch?v=ecshCQU6X2U
# Using Gitbush, setting environment variables in shell
# export X=123;     echo $X : 123 ;     
# to set file with a name 'environment_variables' : vi .environments_variables

#create an auth() function that will have the “Bearer Token” from the app
# doesn't work:   os.environ['TOKEN'] = 'costomer_key'
os.environ ['USER'] = 'Mehmet'
def auth():
    return os.getenv('TOKEN')
auth()

print('\nos.environ:', os.environ) # To see all environment variables on your system

print ('\n os.environ.get(TOKEN) :  ', os.environ.get('TOKEN'))

# To clear a single environment variable in the session, use os.environ.pop() with the key 
# and To clear all environment variables, use os.environ.clear()
os.environ ['USER'] = 'Mehmet'
print( '\nos.environ [USER] Mehmet: ', os.environ.get('USER'))
os.environ.pop('USER')
print( '\nos.environ [USER] Mehmet: ', os.environ.get('USER'))
# os.environ.clear()
print('\nos.environ:', os.environ) 
#-------------------------------------------------------------------------------------
# dotenv reads in environment variables from a file named .env. The file should be formatted as follows:
# api-token = "abcdef_123456"
# Once that’s created and placed in the same folder as your Python file, environment variables can be called like so:
from dotenv import load_dotenv
load_dotenv()
import os
token = os.environ.get("api-token")

