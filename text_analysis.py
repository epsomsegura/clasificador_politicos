#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class Info
----------------
Description
    A class to represent a text analysis 
"""

import re
import nltk
import numpy as np
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

class Text_Analysis:  
    def __init__(self):
        self.lemmas_path = "lemmatization-es.txt"
        self.stopwords = self.getStopwords()
        self.lemmas = self.getLemmas()

    def getStopwords(self):
        sw = stopwords.words("spanish")
        return sw

    def getLemmas(self):
        lemmas = dict()
        fp = open(self.lemmas_path,'r',encoding="utf-8-sig")
        lines = fp.readlines()
        fp.close()
        for i in lines:
            temp = i.rstrip("\n")
            lp = temp.replace("\t","-").split('-')
            lemmas.update({lp[1] : lp[0]})
        return lemmas

    def getTokensBySentence(self,sentence):
        tokens = list()
        toktok = ToktokTokenizer()
        for t in toktok.tokenize(sentence):
            tokens.append(t.lower())
        return tokens

    def stopwordsReduction(self,tokens):
        regexp = r"^[üá-úÁ-Úa-zA-Z0-9]*$"
        i=0
        stopW = self.getStopwords()
        mx = len(tokens)
        while i < mx:
            if re.match(regexp,tokens[i]):
                if tokens[i].lower() in stopW:
                    del tokens[i]
                    mx-=1
                elif tokens[i][0]=="“":
                    tokens[i]=tokens[i].lstrip("“")
            else:
                del tokens[i]
                mx-=1
            i+=1
        return tokens

    def snowballStemmerReduction(self,tokens):
        stemmer = SnowballStemmer("spanish")
        r_tokens=[]
        for i in tokens:
            r_tokens.append(stemmer.stem(i))
        
        return r_tokens

    def lemmaReduction(self,tokens):
        lemmas = self.lemmas
        for i in tokens:
            n=tokens.index(i)
            if i in lemmas.keys():
                tokens[n] = lemmas.get(i)
        return tokens

    def frequencyDistribution(self,tokens):
        freqDist = dict()
        for i in tokens:
            if i in freqDist:
                freqDist[i]+=1
            else:
                freqDist[i]=1
        return sorted(freqDist.items(),key=lambda x:x[1],reverse=True)

    def printFrequencyDistribution(self, freqDist):
        for i in freqDist:
            print(i[0]+'\t'+('' if len(i[0])>15 else '\t')+('\t' if len(i[0])<8 else '')+'=>\t'+str(i[1]))

    def vectorizer(self,raw_text,vectorWords):
        tokenizer = nltk.data.load('tokenizers/punkt/spanish.pickle')
        sentences = tokenizer.tokenize(raw_text)

        #print(sentences)

        vector = []

        counterCommas = 0
        counterPoints = raw_text.count(".")
        countersWordsInSentence = []
        for sentence in sentences:
            counterCommas += sentence.count(",")
            countersWordsInSentence.append(len(self.getTokensBySentence(sentence)))           
            for token in self.getTokensBySentence(sentence):            
                if not token in ["\"","."]:                    
                    vectorWords[token] += 1
        
        vector.append(counterCommas)
        vector.append(counterPoints)

        sumatory = 0
        for counter in countersWordsInSentence:
            sumatory += counter

        averageWordsInSentence = sumatory/len(countersWordsInSentence)

        vector.append(averageWordsInSentence)

        vector.append(len(sentences))

        for word, count in vectorWords.items():
            vector.append(count)

        # número de comas | número de puntos | promedio de palabras por oración | número de oraciones | número de veces que aparece una palabra del conjunto completo en el texto ... 
        return np.array(vector)

    def precision(self,predicted,baseline):
        sumatoryI = 0
        size = len(predicted)
        for i in range(size):
            I = 0
            if predicted[i] == baseline[i]:
                I = 1
            sumatoryI += I
        
        result = (1/size) * sumatoryI

        return result