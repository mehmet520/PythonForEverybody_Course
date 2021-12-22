
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
import oauth
import hidden

oauth()
def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def create_url(keyword, start_date, end_date, max_results = 10):
    
    search_url = "https://api.twitter.com/2/tweets/search/all" #Change to the endpoint you want to collect data from

    #change params based on the endpoint you are using
    query_params = {'query': keyword,
                    'start_time': start_date,
                    'end_time': end_date,
                    'max_results': max_results,
                    'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
                    'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
                    'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
                    'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
                    'next_token': {}}
    return (search_url, query_params)

# Connect to Endpoint
# Now that we have the URL, headers, and parameters we want, we will create a function that will put all of this together and connect to the endpoint.
# The function below will send the “GET” request and if everything is correct (response code 200), it will return the response in “JSON” format.
# Note: next_token is set to “None” by default since we only care about it if it exists.
def connect_to_endpoint(url, headers, params, next_token = None):
    params['next_token'] = next_token   #params object received from create_url function
    response = requests.request("GET", url, headers = headers, params = params)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

#    Putting it all Together
# Now that we have all the functions we need, let's test putting them all together to create our first request!
# In the next cell, we will set up our inputs:
# bearer_token and headers from the API.
# We will look for tweets in English that contain the word “xbox”.
# We will look for tweets between the 1st and the 31st of March, 2021.
# We want only a maximum of 15 tweets returned.
#The end_time and start_time format that Twitter uses for timestamps is
# YYYY-MM-DDTHH:mm:ssZ
#Inputs for the request
bearer_token = oauth.get('bearer_token')
headers = create_headers(bearer_token)
keyword = "xbox lang:en"
start_time = "2021-03-01T00:00:00.000Z"
end_time = "2021-03-31T00:00:00.000Z"
max_results = 15

#Now we will create the URL and get the response from the API.
# The response returned from the Twitter API is returned in JavaScript Object Notation “JSON” format.
#If the returned response from the below code is 200, then the request was successful.
url = create_url(keyword, start_time,end_time, max_results)
json_response = connect_to_endpoint(url[0], headers, url[1])

#Lets print the response in a readable format using this JSON library functions
print(json.dumps(json_response, indent=4, sort_keys=True))