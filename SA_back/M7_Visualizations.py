from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
#from M3_SA_Handler import PT_df, NT_df, Neut_df
#from M6_lemm_Wordlist import Word_Cloud_String
import matplotlib.pyplot as plt
#from app import User_word
import io


def Pie_Plot(PT_df, NT_df, Neut_df, User_word):
    # Pie Plot of Positive, Negative and Neutral Tweets
    Area=[len(PT_df), len(NT_df), len(Neut_df)]
    boom=(0,0,0.1)
    labels='Positive Tweets', 'Negative Tweets', 'Neutral Tweets'
    plt.pie(Area, explode=boom,labels= labels, colors=['green', 'red', 'yellow'], autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.title('Percentage of Tweets Sentiment for '+ User_word)
    plt.show()

    # b1_image = io.BytesIO()
    # plt.savefig(b1_image, format='png')
    # b1_image.seek(0)
    # return b1_image



# #Plot of "Sentiment Polarity vs Number of tweets"
# figure, axes= plt.subplots(figsize=(6,6))
# PN_sentiment_df.hist(bins=[-1, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1], ax=axes, color= ['r'])
# #Plot Xlabel ylabel and title
# plt.xlabel('More Negative<--------------->More Positive')
# plt.ylabel('Number of Tweets on %s' %User_word)
# plt.title('People Sentiment on %s (Globally)' %User_word)
# #Remove grid and tick labels
# plt.grid(b=None)
# axes.set_ylabel('Tweets Count')
# axes.set_yticklabels([])
# plt.yticks([])
# #Show plot
# plt.show()

def Word_Cloud(Word_Cloud_String):
    #Creating Word Cloud    
    sw = set(STOPWORDS)
    wordcloud = WordCloud(width=1600, height=900, stopwords=sw, min_font_size=25).generate(Word_Cloud_String)
    plt.figure(figsize=(12,12), facecolor= 'k')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    #plt.show()

    # b2_image = io.BytesIO()
    # plt.savefig(b2_image, format='png')
    # b2_image.seek(0)
    # return b2_image

# if __name__=="__main__":
#         Pie_Plot()
#         Word_Cloud()
