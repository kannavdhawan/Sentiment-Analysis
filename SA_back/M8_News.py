import requests
from bs4 import BeautifulSoup 
import json
import pandas as pd

# def News():
#     url = 'https://inshorts.com/en/read'
#     response = requests.get(url)

#     #print(response)
#     Recent_News=[]
#     def print_headlines(response_text):
#         soup = BeautifulSoup(response_text, 'lxml')
#         headlines = soup.find_all(attrs={"itemprop": "headline"})
#         for headline in headlines:
#             News = headline.text
#             Recent_News.append(News)
#             #print(News)
#         #return News

#     print_headlines(response.text)

def News():
    url = 'https://inshorts.com/en/read'
    response = requests.get(url)

    #print(response)
    Recent_News=[]
    soup = BeautifulSoup(response.text, 'lxml')
    headlines = soup.find_all(attrs={"itemprop": "headline"})
    for headline in headlines:
        News = headline.text
        Recent_News.append(News)
    
    # News_df = pd.DataFrame(Recent_News)
    # print(News_df)
    #Recent_News = News_df.to_dict()
    #print(Recent_News)
    #return Recent_News
    return Recent_News

News()