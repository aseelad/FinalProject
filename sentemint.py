##get the sentemint 
from __future__ import division
import urllib
from string import punctuation
import os
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import unicodedata
import nltk
##read postitve words
pos_sent = open("positive.txt").read()
positive_words=pos_sent.split('\n')

##read negative words
neg_sent = open('negative.txt').read()
negative_words=neg_sent.split('\n')

# read all articles
Newspapers=["nytimes.com","thejakartapost.com","reuters.com","champress.net","timesofindia.indiatimes.com", "aawsat.net", "english.people.com.cn" ,"bbc.co.uk" ,"tehrantimes.com","dw.de"]

for news in Newspapers:
    rootdir ="/Users/Aseel/FinalProject/GayRights/"+news+"/"
    count=0
    W=[]
    positive_counts=[]
    negative_counts=[]
    for subdir, dirs, files in os.walk(rootdir):
        for fi in files:
            if fi == '.DS_Store':
                continue  # skip the file
            u= os.path.join(subdir, fi)
            f = open(u, 'r')
            text = f.read()
            lowers = text.lower()
            #remove the punctuation using the character deletion step of translate
            no_punctuation = lowers.translate(None, string.punctuation)
            tokens = nltk.word_tokenize(no_punctuation)
            W.extend(tokens)

        positive_counter=0
        negative_counter=0
    
        word_count=len(W)
        for word in W:
            if word in positive_words:
                positive_counter=positive_counter+1
            elif word in negative_words:
                negative_counter=negative_counter+1
        
        if positive_counter ==0 or negative_counter==0:
        	continue
        positive_counts=positive_counter/word_count
        negative_counts=negative_counter/word_count
        
        if positive_counts > negative_counts:
            Sentmenint="Pos " + str(positive_counts)
        
        if positive_counts < negative_counts:
            Sentmenint="Neg" + str(negative_counts)
        
        if positive_counts == negative_counts:
            Sentmenint="Natural" + str(positive_counts)
        #save to file
        f = open("/Users/Aseel/FinalProject/GayRights/"+news+"_Sentmenint.txt", "w")
        f.write(str(Sentmenint))
        f.close()

