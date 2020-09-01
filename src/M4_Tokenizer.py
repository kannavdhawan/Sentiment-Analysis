import pandas as pd
from nltk.tokenize import TweetTokenizer
from multiprocessing import Process
from nltk.corpus import stopwords
from string import punctuation
import collections
#from M0_main import User_word
#from M3_SA_Handler import PT_list, NT_list

Custom_words= set(stopwords.words('english') + list(punctuation))
Custom_words.update(['..','...','....', 'has', 'have', "hasn't", "haven't", 'there', 'their', 'a', 'i', 'the', 'A', 'THE', 'I', 'why', "isn't"
'was', 'then', 'than','im', 'IM', 'many', 'much', 'more'])

#Collection_words=[User_word.lower()] 

def Pos_Tokenizer(PT_list, User_word):
    ##Analysis for Positive Tweets
    #Tokenization using TweetTokenizer()
    PTW_list= [TweetTokenizer().tokenize(sentence) for sentence in PT_list]

    #Remove Stopwords using ntlk stopwords and punctuation
    PSense_words=[]
    for each_sentence_list in PTW_list:
        for each_word in each_sentence_list:
            if each_word not in Custom_words:
                PSense_words.append(each_word)

    #Lowr case all the letters which will help in finding unique characters
    psense_words= [every_word.lower() for every_word in PSense_words]

    #Remove collection words
    Nokeyword_Pwordlist=[]
    for word in psense_words:
        if word not in User_word.lower():
            Nokeyword_Pwordlist.append(word)

    return Nokeyword_Pwordlist  #obj5

#Nokeyword_Pwordlist = Pos_Tokenizer()
#print('Positive:\n', Nokeyword_Pwordlist)

def Neg_Tokenizer(NT_list, User_word):
    #Tokenization using TweetTokenizer()
    NTW_list= [TweetTokenizer().tokenize(sentence) for sentence in NT_list]
    #print(NTW_list)

    #Remove Stopwords using ntlk stopwords and punctuation
    NSense_words=[]
    for every_sentence in NTW_list:
        for every_word in every_sentence:
            if every_word not in Custom_words:
                NSense_words.append(every_word)

    #Lowr case all the letters which will help in finding unique characters
    nsense_words= [every_word.lower() for every_word in NSense_words]

    #Remove collection words
    Nokeyword_Nwordlist=[]
    for w in nsense_words:
        if w not in User_word.lower():
            Nokeyword_Nwordlist.append(w)

    return Nokeyword_Nwordlist              #obj6

#Nokeyword_Nwordlist = Neg_Tokenizer()
#print('Negative:\n', Nokeyword_Nwordlist)

# if __name__=="__main__":
#     p1 = Process(target=Pos_Tokenizer)
#     p1.start()

#     p2 = Process(target=Neg_Tokenizer)
#     p2.start()

