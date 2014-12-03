##preporcessing
##cleaning the data
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import string
import os
import unicodedata


##get text file
Newspapers=["nytimes.com","thejakartapost.com","reuters.com"]
for news in Newspapers:
    tokenized_docs =[]
    rootdir ="/Users/Aseel/FinalProject/islamicstate/"+news+"/"
    for subdir, dirs, files in os.walk(rootdir):
        for fi in files:
            if fi == '.DS_Store':
                continue  # skip the file
            u= os.path.join(subdir, fi)
            f = open(u, 'r').read()
            tokenized_docs.extend(word_tokenize(f.decode('utf-8')))
    ##Removing punctuation
    regex = re.compile('[%s]' % re.escape(string.punctuation)) #see documentation here: http://docs.python.org/2/library/string.html
    tokenized_docs_no_punctuation = []
    for token in tokenized_docs: 
        new_token = regex.sub(u'', token)
        if not new_token == u'':
            tokenized_docs_no_punctuation.append(new_token)

    
    ##remove stop words
    tokenized_docs_no_stopwords = []
    for word in tokenized_docs_no_punctuation:
        if not word in stopwords.words('english'):
            tokenized_docs_no_stopwords.append(word)
    
    
    ##write the update version to a file
    f = open(rootdir+"_Updated.txt", "w")
    for word in tokenized_docs_no_stopwords:
        word=unicodedata.normalize('NFKD', word).encode('ascii','ignore')
        f.write(str(word)+" ")
        #f.write("\n")
    f.close()

