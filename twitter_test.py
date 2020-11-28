import os
import tweepy as tw
import pandas as pd

consumer_key= input("Enter consumer key: ")
consumer_secret= input("Enter consumer secret: ")
access_token= input("Enter access token: ")
access_token_secret= input("Enter access token secret: ")

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Define the search term and the date_since date as variables
search_words = "facebook"
date_since = "2020-11-25"

# Collect tweets
tweets = tw.Cursor(api.search,q=search_words,lang="en",since=date_since)

users_locs = [[tweet.user.screen_name, tweet.user.location] for tweet in tweets]
tweet_text = pd.DataFrame(data=users_locs,columns=['user', "location"])

print(tweet_text.shape)
