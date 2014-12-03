import os


Newspapers=["champress.net","timesofindia.indiatimes.com", "aawsat.net", "english.people.com.cn" ,"bbc.co.uk" ,"tehrantimes.com"
            ,"dw.de"]
            
for news in Newspapers:
	d = os.path.dirname("/Users/Aseel/FinalProject/islamicstate/"+news+"/")
	if not os.path.exists(d):
		os.makedirs(d)


