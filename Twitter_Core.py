#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tweepy

class Twitter_Core:

    def load_keys(self,filename):
        keys = dict()
        with open(filename) as f:
            line = f.readline()
            while line: 
                keys[line.split(':')[0].strip()] = line.split(':')[1].strip()
                line = f.readline()
        return keys

    def recover_tweets(self,keys,query,limit):
        consumer_key = keys["consumer_key"]
        consumer_secret = keys["consumer_secret"]
        access_token = keys["access_token"]
        access_token_secret = keys["access_token_secret"]

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)
        tweets = tweepy.Cursor(api.search,query,lang="es",tweet_mode="extended",wait_on_rate_limit=True).items(limit)
        return tweets

    def format(self,tweets):
        format_tweets = []
        for tweet in tweets:
            temp_dict = dict()
            temp_dict["user"] = tweet.user.screen_name
            temp_dict["text"] = tweet.full_text
            format_tweets.append(temp_dict)
        return format_tweets