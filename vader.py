# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 17:23:34 2018

@author: JARVIS
"""
#change working directory
import os
os.chdir("C://Users//JARVIS//Desktop//Uni//Thesis//data scraping//BachelorProject")


#Get data
import pandas
df = pandas.read_csv('alldatanosent.csv',encoding = "ISO-8859-1")

#check that data is actually there
print(df)

#define variables
datetime=[]
name=[]
tweet = []
vs_compound = []
vs_pos = []
vs_neu = []
vs_neg = []

#loading lexicon and other stuff
import vaderSentiment

#importing the main tool
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#calling the sentiment analysis tool something shorter
analyzer = SentimentIntensityAnalyzer()

#go through the data with the tool and append results to variables defined earlier
for index, row in df.iterrows():
    dates=(row["Datetime"])
    texts=(row["Text"])
    names=(row["ID"])
    datetime.append(dates)
    name.append(names)
    tweet.append(texts)
    vs_compound.append(analyzer.polarity_scores(texts)['compound'])
    vs_pos.append(analyzer.polarity_scores(texts)['pos'])
    vs_neu.append(analyzer.polarity_scores(texts)['neu'])
    vs_neg.append(analyzer.polarity_scores(texts)['neg'])

#now composing variables with values into a dataframe
from pandas import Series, DataFrame

twitter_df = DataFrame({'Datetime': datetime,
                        'Name': name,
                        'Tweet': tweet,
                        'Compound': vs_compound,
                        'Positive': vs_pos,
                        'Neutral': vs_neu,
                        'Negative': vs_neg})




# Have a look at the top 5 results.
twitter_df.head()

#all good, can write csv, all future work is in R 
twitter_df.to_csv('alldatasent.csv')

