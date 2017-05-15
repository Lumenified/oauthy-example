#!/usr/bin/python

import json
import oauth2 as oauth

consumer_key=   "" #here is the consumer key that is provided by twitter for the app
consumer_secret=    "" #here is the consumer secret that is provided by twitter for our app

access_token=   "" #here goes the token key

access_token_secret=    "" #token secret you guessed right, from twitter

consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
access_token = oauth.Token(key=access_token, secret=access_token_secret)
client = oauth.Client(consumer, access_token)


timeline_endpoint = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=LadyCadashing&count=1"

response, data = client.request(timeline_endpoint)

tweets = json.loads(data)

for tweet in tweets:
    """the output will be the text in this condition which is the requested person's tweet,"""
    print tweet['text']
    #print data
