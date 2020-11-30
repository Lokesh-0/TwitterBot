#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tweepy
import time

key = '####'
secret = '####'
consumer_key = '####'
consumer_secret = '####'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

hashtag = 'Neymar'
tweetnumber = 5000
tweets = tweepy.Cursor(api.search, hashtag).items(tweetnumber)

def searchbot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Done!")
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)

searchbot()

