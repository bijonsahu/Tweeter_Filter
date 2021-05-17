# Twitter API authentication

import tweepy
import Twitter_Credentials as tc
api_key = tc.api_key
api_secret_key = tc.api_secret_key
access_token = tc.access_token
access_token_secret = tc.access_token_secret

# authorize the API Key
authentication = tweepy.OAuthHandler(api_key, api_secret_key)

# authorization to user's access token and access token secret
authentication.set_access_token(access_token, access_token_secret)

# call the api
api = tweepy.API(authentication)