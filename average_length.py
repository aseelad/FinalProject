## get the average length of all article for each newspaper
import nltk
import string
import os
from collections import Counter
from nltk.corpus import stopwords

# read all articles
Newspapers=["nytimes.com","thejakartapost.com","reuters.com","champress.net","timesofindia.indiatimes.com", "aawsat.net", "english.people.com.cn" ,"bbc.co.uk" ,"tehrantimes.com","dw.de"]

for news in Newspapers:
    rootdir ="/Users/Aseel/FinalProject/GayRights/"+news+"/"
    Counting=[]
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
            count= len(tokens)
            #get the count of words
            Counting.append(int(count))
        if len(Counting) ==0:
        	continue
        #get the average 
        sum=0
        average=0
        for n in Counting:            
            sum = sum + n
        average = sum / len(Counting)
        #save to file
        f = open("/Users/Aseel/FinalProject/GayRights/"+news+"_average.txt", "w")
        f.write(str(average))
        f.close()
