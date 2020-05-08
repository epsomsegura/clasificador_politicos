#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import pickle
import nltk
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from nltk.tokenize.toktok import ToktokTokenizer
from Twitter_Core import Twitter_Core
from Text_Analysis import Text_Analysis


#recover the most recent 1000 tweets from twitter
twitter_core = Twitter_Core()
keys = twitter_core.load_keys("Keys.txt")
tweets = twitter_core.recover_tweets(keys,"Lopez Obrador -filter:retweets",50)
tweets = twitter_core.format(tweets)

#Tranforming json_data to vectorize
corpus_data = []
with open("training_corpus.json") as json_file:
    corpus_data_temp = []
    for line in json_file.readlines():
        corpus_data_temp.append(json.loads(line))
    for line in corpus_data_temp:    
        i = 0    
        for corpus_tweet in line["text"]:
            if i == 50:
                break
            temp_row = dict()
            temp_row["gender"] = line["gender"]
            temp_row["age_group"] = line["age_group"]
            temp_row["text"] = corpus_tweet
            corpus_data.append(temp_row)      
            i += 1  

txta = Text_Analysis()

#Creating or restoring vectorial space
exists_vectorial_space = True
try:
    f = open("vectorial_space.obj")
except:
    exists_vectorial_space = False

print("processing tokens")
tokens = []
if exists_vectorial_space:
    pickle_in = open("vectorial_space.obj","rb")
    tokens = pickle.load(pickle_in)
else:    
    tokens = []
    for tweet in corpus_data:
        tokenizer = nltk.data.load('tokenizers/punkt/spanish.pickle')
        sentences = tokenizer.tokenize(tweet["text"])
        for sentence in sentences:            
            temp_tokens = txta.getTokensBySentence(sentence)
            for temp_token in temp_tokens:
                if not temp_token in tokens:            
                    tokens.append(temp_token)
                    
    #tokens = txta.snowballStemmerReduction(txta.stopwordsReduction(tokens))    
    pickle_out = open("vectorial_space.obj","wb")
    pickle.dump(tokens, pickle_out)
    pickle_out.close()

print("Adding new tweets to vectorial space")
# Adding tweets donwloaded
for tweet in tweets:
    tokenizer = nltk.data.load('tokenizers/punkt/spanish.pickle')
    sentences = tokenizer.tokenize(tweet["text"])
    for sentence in sentences:
        temp_tokens = txta.getTokensBySentence(sentence)
        for temp_token in temp_tokens:
            if not temp_token in tokens:
                tokens.append(temp_token)    

print("Training logreg")
#Regresión Lógistica
tokensDict = dict()
for token in tokens:
    tokensDict[token] = 0

df = pd.DataFrame(corpus_data)

X_raw = df['text']
X_vectors = np.array([])
for i in range(len(X_raw)):
    if len(X_vectors) == 0:        
        X_vectors = txta.vectorizer(X_raw[:].iloc[i],tokensDict.copy())
    else:
        X_vectors = np.vstack([X_vectors,txta.vectorizer(X_raw[:].iloc[i],tokensDict.copy())])

y = df['gender'].to_numpy()
X_train, X_test, y_train, y_test = train_test_split(X_vectors,y,test_size=0.3,random_state=101)

logreg = LogisticRegression()
logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)

print(y_test)
print(y_pred)

print('\nPrecisión Regresión: {0}'.format(txta.precision(y_pred, y_test)))

df2 = pd.DataFrame(tweets)
n_X_raw = df2['text']
n_X_vectors = np.array([])
for i in range(len(n_X_raw)):
    if len(n_X_vectors) == 0:        
        n_X_vectors = txta.vectorizer(n_X_raw[:].iloc[i],tokensDict.copy())
    else:
        n_X_vectors = np.vstack([n_X_vectors,txta.vectorizer(n_X_raw[:].iloc[i],tokensDict.copy())])
n_y_pred = logreg.predict(n_X_vectors)

print(n_y_pred)

"""
for tweet in corpus_data:    
    print(tweet)
    print("----------------------------------------------------")
print(len(corpus_data))
"""
for tweet in tweets:
    tweet["frecdist"] = txta.frequencyDistribution(txta.snowballStemmerReduction(txta.stopwordsReduction(txta.getTokensBySentence(tweet["text"]))))
    print(tweet)
    print("----------------------------------------------------")
print(len(tweets))
