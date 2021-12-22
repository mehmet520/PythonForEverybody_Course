import urllib.request, urllib.parse, urllib.error
import oauth
import hidden
import twitter


# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

def augment(url, parameters):
    secrets = hidden.oauth()
    # api = twitter.Api(consumer_key='consumer_key',
    #                   consumer_secret='consumer_secret',
    #                   access_token_key='access_token',
    #                   access_token_secret='access_token_secret')
    # api = twitter.Api(consumer_key= secrets['consumer_key'],
    #                 consumer_secret= secrets['consumer_secret'],
    #                 access_token_key= secrets['access_token_key'],
    #                 access_token_secret=secrets['access_token_secret'])      

            
    consumer = oauth.OAuthConsumer(secrets['consumer_key'],
                                   secrets['consumer_secret'])
    token = oauth.OAuthToken(secrets['access_token_key'], secrets['access_token_secret'])

    oauth_request = oauth.OAuthRequest.from_consumer_and_token(consumer,
                    token=token, http_method='GET', http_url=url,
                    parameters=parameters)
    oauth_request.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(),
                               consumer, token)
    return oauth_request.to_url()
