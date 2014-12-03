##get the count of all words in each newspapers
import nltk
import string
import os
from collections import Counter
from nltk.corpus import stopwords

Newspapers=["nytimes.com","thejakartapost.com","reuters.com","champress.net","timesofindia.indiatimes.com", "aawsat.net", "english.people.com.cn" ,"bbc.co.uk" ,"tehrantimes.com","dw.de"]

for news in Newspapers:
    rootdir ="/Users/Aseel/FinalProject/GayRights/"+news+"/"
    words=[]
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
            tokens =nltk.word_tokenize(no_punctuation)
            words.extend(tokens)
    count = Counter(words)

    filtered = [w for w in words if not w in stopwords.words('english')]
    count = Counter(filtered)
    most_common= count.most_common(20)
    #save to file
    f = open("/Users/Aseel/FinalProject/GayRights/"+news+"_most_common.txt", "w")
    for item in most_common:
        f.write(str(item))
        f.write("\n")
    f.close()
