## Authentication Handler and  Tweet Fetchers Module

import tweepy as tw
from tweepy import OAuthHandler, StreamListener, Stream
import pandas as pd                                                    
import datetime
from multiprocessing import Process
from threading import Thread
import sys

def TweetText_fetcher(keyword_tweets):
    Full_tweets= []
    tweets_text=[]
    
    for each_tweet in keyword_tweets:
        Full_tweets.append(each_tweet)
        tweets_text.append(each_tweet.full_text)

    #print(Full_tweets)
    #print('+++++++++++++++++++++++++++++++++++++++++++++++')
    #print('Tweet Text:\n', tweets_text)
    return tweets_text

def TweetCountry_fetcher(keyword_tweets):
    tweets_location=[]
    for tweet in keyword_tweets:
        tweets_location.append(tweet.user.location)
    
    print('\nTweet Locations:\n', tweets_location)
    return tweets_location

if __name__=="__main__":
    
    p1 = Process(target=TweetText_fetcher)
    p1.start()
    
    p2 = Process(target=TweetCountry_fetcher)
    p2.start()

    

   
   