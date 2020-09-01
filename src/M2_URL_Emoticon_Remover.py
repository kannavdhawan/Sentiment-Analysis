## URL and Emoticon Removal Module

import pandas as pd
#from M1_Auth_Fetcher import T
import re

def URL_Emoticon_Cleaner(obj2):
    df_Text=pd.DataFrame({'Text': obj2})
    df_Text= df_Text.replace(to_replace=r'https?:\/\/.*[\r\n]*',value='',regex=True)    #Remove URLS
    df_Text= df_Text.replace(to_replace=[r'\d+', '$', '@', ',', '/', '&', '#', '!', '_',';', ':','\n', '\t','^A-Za-z0-9','"', '|',' - ', '-'], value='',regex=True)
   
    #Dataframe to List conversion
    filtered_tweets= df_Text.values.tolist()

    i=0
    CT = [tweet[i].encode('ascii', 'ignore').decode('ascii') for tweet in filtered_tweets]
    #print('Cleaned Tweets:\n', CT)
    return CT

#Cleaned_Tweets = URL_Emoticon_Cleaner()

#if __name__=="__main__":
    #URL_Emoticon_Cleaner()