###get the total number of articles for each newspaper

# read all articles
import os
Newspapers=["nytimes.com","thejakartapost.com","reuters.com","champress.net","timesofindia.indiatimes.com", "aawsat.net", "english.people.com.cn" ,"bbc.co.uk" ,"tehrantimes.com","dw.de"]
for news in Newspapers:
    rootdir ="/Users/Aseel/FinalProject/GayRights/"+news+"/"
    count=0
    for subdir, dirs, files in os.walk(rootdir):
        for fi in files:
            if fi == '.DS_Store':
                continue  # skip the file
            count=count+1    
    #save to file
    f = open("/Users/Aseel/FinalProject/GayRights/"+news+"_ArticleCount.txt", "w")
    f.write(str(count))
    f.close()

