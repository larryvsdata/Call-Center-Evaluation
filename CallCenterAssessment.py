#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 22:32:43 2018

@author: ermanbekaroglu
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 18:52:55 2018

@author: ermanbekaroglu
"""
import speech_recognition as sr
import nltk
import numpy as np
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

class CCEvaluation():
    
    def __init__(self):
        self.heySay="Say something!"
        self.sphinxThinks="Sphinx thinks you said:  "
        self.sphinxUnable="Unable to understand. "
        self.r=sr.Recognizer()
        self.positives = []
        self.negatives = []
        self.Text=None
        self.sentimentValue=None

        
        
    def dfToList(self,dfToBeConverted):
        resultList=list(dfToBeConverted)
        resultList+=(list(dfToBeConverted[resultList[0]]))
        return resultList

    def positivesNegatives(self):
        self.positives=self.dfToList(pd.read_csv("words-positive.csv"))
        self.negatives=self.dfToList(pd.read_csv("words-negative.csv"))
        
    def avgSentiment(self,text):
        self.positivesNegatives()
        temp=[]
        text_sent=nltk.sent_tokenize(text)
        for sentence in text_sent:
            n_count=0
            p_count=0
            
            sent_words=nltk.word_tokenize(sentence)
            
            for word in sent_words:
                if word.lower() in self.positives:
                        p_count+=1
                if word.lower() in self.negatives:
                        n_count+=1
                        
            if (p_count>0 and n_count==0):
                temp.append(1)
            elif n_count%2>0:
                temp.append(-1)
            
            elif (n_count%2==0 and n_count>0):
                temp.append(1)
            else:
                temp.append(0)
        return round(np.average(temp),2)
    
    
    def outputSentiment(self):
        if self.Text!=None:
            self.sentimentValue=self.avgSentiment(self.Text)
            print('Average sentiment value is: '+str(self.sentimentValue))
        
        
    

        
        
        

    def getTheSpeech(self):
        with sr.Microphone() as source:
            print(self.heySay)
            audio=self.r.listen(source)
            
            try:
                self.Text=self.r.recognize_sphinx(audio)
                print(self.sphinxThinks+self.Text)
            except:
                print(self.sphinxUnable)
        
    
if __name__ == "__main__":

    CCenter= CCEvaluation()
    CCenter.getTheSpeech()
    CCenter.outputSentiment()
  