from __future__ import division

##TF-IDF 

import math
from textblob import TextBlob as tb
 
def tf(word, blob):
    return blob.words.count(word) / len(blob.words)
 
def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)
 
def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))
 
def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)
 
  
  
  
Newspapers=["nytimes.com","thejakartapost.com","reuters.com"]
bloblist=[]
for news in Newspapers:
    f = open("/Users/Aseel/xgoogle/islamicstate/"+news+"_Updated.txt", 'r')
    blob = tb(f.read())
    bloblist.append(blob)

scores = {}
for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    print len(blob.words)

    for word in blob.words:
    	scores = {word: tfidf(word, blob, bloblist)}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:20]:
        print("Word: {}, TF-IDF: {}".format(word, round(score, 5)))
    
