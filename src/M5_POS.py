## POS Tagger
import spacy
#from M4_Tokenizer import Nokeyword_Pwordlist, Nokeyword_Nwordlist
import nltk
import pandas as pd
from multiprocessing import Process 

nlp = spacy.load("en_core_web_sm")

def Pos_Tagger(obj5):
    PTags=[]
    for pt in obj5:
        P_tokens = nlp(pt)
        for P_token in P_tokens:
            tabs= (pt, P_token.pos_)
            PTags.append(tabs)
    #print('Spacy Tag Result of Positive Tweet words:\n', PTags)
    #print('+++++++++++++++++++++++++++++++++++++++++++++++++++++')

    #Converting Positive and NEgative words with their tags to respective Dataframes
    P_Tags_df= pd.DataFrame(PTags, columns=['Pword', 'Tag'])
    #print('Positive words with tags:\n', P_Tags_df)

    #Set Index as PWord to classify Noun, Adjective and Verb Tags
    P_Tags_df= P_Tags_df.set_index('Pword')

    Pnoun_Tags_df= P_Tags_df.loc[P_Tags_df['Tag'] == 'NOUN']
    Pverb_Tags_df= P_Tags_df.loc[P_Tags_df['Tag'] == 'VERB']
    Padj_Tags_df= P_Tags_df.loc[P_Tags_df['Tag'] == 'ADJ']

    Pnoun_Tags_df=Pnoun_Tags_df.reset_index()
    Pverb_Tags_df=Pverb_Tags_df.reset_index()
    Padj_Tags_df=Padj_Tags_df.reset_index()

    Pnoun_words_df= Pnoun_Tags_df.iloc[:,0]
    Pverb_words_df= Pverb_Tags_df.iloc[:,0]
    Padj_words_df= Padj_Tags_df.iloc[:,0]

    Pnoun_list= Pnoun_words_df.values.tolist()
    Pverb_list= Pverb_words_df.values.tolist()
    Padj_list= Padj_words_df.values.tolist()

    return Pnoun_list, Pverb_list, Padj_list

# Pnoun_list = Pos_Tagger()[0]
# Pverb_list = Pos_Tagger()[1]
# Padj_list = Pos_Tagger()[2]

# print('Positive Nouns: ', Pnoun_list)
# print('\nPositive Verb: ', Pverb_list)
# print('\nPositive Adj: ', Padj_list)

#-------------------------------------------------------------------------------------------

def Neg_Tagger(obj6):
    NTags=[]
    for nt in obj6:
        N_tokens = nlp(nt)
        for N_token in N_tokens:
            tabs= (nt, N_token.pos_)
            NTags.append(tabs)
    #print('Spacy Tag Result of Negative Tweet words:\n', NTags)

    #Converting Positive and NEgative words with their tags to respective Dataframes
    N_Tags_df= pd.DataFrame(NTags, columns=['Nword', 'Tag'])
    #print('Negative words with tags:\n', N_Tags_df)

    N_Tags_df= N_Tags_df.set_index('Nword')

    Nnoun_Tags_df= N_Tags_df.loc[N_Tags_df['Tag'] == 'NOUN']
    Nverb_Tags_df= N_Tags_df.loc[N_Tags_df['Tag'] == 'VERB']
    Nadj_Tags_df= N_Tags_df.loc[N_Tags_df['Tag'] == 'ADJ']

    Nnoun_Tags_df=Nnoun_Tags_df.reset_index()
    Nverb_Tags_df=Nverb_Tags_df.reset_index()
    Nadj_Tags_df=Nadj_Tags_df.reset_index()

    Nnoun_words_df= Nnoun_Tags_df.iloc[:,0]
    Nverb_words_df= Nverb_Tags_df.iloc[:,0]
    Nadj_words_df= Nadj_Tags_df.iloc[:,0]

    Nnoun_list= Nnoun_words_df.values.tolist()
    Nverb_list= Nverb_words_df.values.tolist()
    Nadj_list= Nadj_words_df.values.tolist()

    return Nnoun_list, Nverb_list, Nadj_list


# # Nnoun_list = Neg_Tagger()[0]
# # Nverb_list = Neg_Tagger()[1]
# # Nadj_list = Neg_Tagger()[2]

# # print('\nNegative Nouns: ', Nnoun_list)
# # print('\nNegative Verb: ', Nverb_list)
# # print('\nNegative Adj: ', Nadj_list)

# # if __name__=="__main__":
# #    Pos_Tagger()
# #    Neg_Tagger()