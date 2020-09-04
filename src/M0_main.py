import tweepy as tw
from tweepy import OAuthHandler, StreamListener, Stream
import pandas as pd                                                    
import datetime
from multiprocessing import Process
from threading import Thread
import sys
import io
#from app import word
from M1_Auth_Fetcher import TweetText_fetcher
from M2_URL_Emoticon_Remover import URL_Emoticon_Cleaner
from M3_SA_Handler import Sentiment_Analyzer
from M4_Tokenizer import Pos_Tokenizer, Neg_Tokenizer
from M5_POS import Pos_Tagger, Neg_Tagger
from M6_lemm_Wordlist import Pos_lemm, Neg_lemm, Wordlist
from M7_Visualizations import Pie_Plot, Word_Cloud
#from app import wordcloud
from M8_News import News


def code(X):
    #Connect with Twitter API
    consumer_key='HJ0eUYLpsznZCHcFMj21Va1UX'
    consumer_secret='o8VyPWxlZEFv6vlmZVxnMYe2FnNcfxrYUw9Ow32eUM81VNYKlk'
    access_token='1217185233029795840-2pH6yQr8aMkCUuy8QLrjnM40poKBqU'
    access_secret='czr0hFCk8sTPMipO8zvkOkrcpEUoUSMEn7P9CuAdiponr'

    class data_listener(StreamListener):                                        #Class to print data and errors
        def on_data(self, data):
            print (data)
            return True
            
        def on_error(self, status):
            print (status)

    d_file= data_listener()                                     #Putting the captured data in variable d_file
    auth= tw.OAuthHandler(consumer_key, consumer_secret)        #Create OAuth  Handler
    auth.set_access_token(access_token, access_secret)          #Setting tokens
    api= tw.API(auth, wait_on_rate_limit=True)                  #Establishing connection through Tweepy to Twitter API i.e. 'api' is the introductory point now.
    data_pipeline= Stream(auth, d_file)

    User_word= str(X)
    keyword= User_word + '-filter:retweets'  #Filter:Media for images and videos 
    keyword_tweets= tw.Cursor(api.search, q=keyword, lang='en', tweet_mode= 'extended', since=(datetime.date.today() - datetime.timedelta(days=7))).items(100)
    #print(keyword_tweets)

    obj4=[]

    obj2 = TweetText_fetcher(keyword_tweets)
    obj3 = URL_Emoticon_Cleaner(obj2)
    obj4 = Sentiment_Analyzer(obj3)
    

    PT_list = obj4[0]
    NT_list = obj4[1]
    PT_df = obj4[2]
    NT_df = obj4[3]
    Neut_df = obj4[4]
    Pie_dict = obj4[5]


    obj5 = Pos_Tokenizer(PT_list, User_word)
    obj6 = Neg_Tokenizer(NT_list, User_word)
    
    ##M5_POS
    obj7=[]
    obj7 = Pos_Tagger(obj5)
    Pnoun_list = obj7[0]
    Pverb_list = obj7[1]
    Padj_list = obj7[2]


    ##M5_POS
    obj8=[]
    obj8 = Neg_Tagger(obj6)
    Nnoun_list = obj8[0]
    Nverb_list = obj8[1]
    Nadj_list = obj8[2]


    obj9=[]
    obj9 = Pos_lemm(Pnoun_list, Pverb_list, Padj_list)
    PC_noun_words = obj9[0]
    PC_verb_words = obj9[1]
    PC_adj_words = obj9[2]


    obj10=[]
    obj10 = Neg_lemm(Nnoun_list, Nverb_list, Nadj_list)
    NC_noun_words = obj10[0]
    NC_verb_words = obj10[1]
    NC_adj_words = obj10[2]

    WC_dict = Wordlist(PC_noun_words, NC_noun_words, PC_verb_words, NC_verb_words, PC_adj_words, NC_adj_words)

    Recent_News = News()

    temp={}

    temp["Pie_Chart"] = Pie_dict
    temp["Word_Cloud"] = WC_dict
    temp["News"] = Recent_News

    

    return temp




