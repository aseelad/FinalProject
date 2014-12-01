import os


Newspapers=["nytimes.com","champress.net","timesofindia.indiatimes.com", "aawsat.net", "english.people.com.cn" ,"bbc.co.uk" ,"tehrantimes.com"
            ,"dw.de","thejakartapost.com","reuters.com"]
            
for news in Newspapers:
	d = os.path.dirname("/Users/Aseel/xgoogle/GayRights/"+news+"/")
	if not os.path.exists(d):
		os.makedirs(d)


