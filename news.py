## read URL from text file and get the article text 


import newspaper
from newspaper import Article

Newspapers=["nytimes.com"]
            
for news in Newspapers:
	f = open('/Users/Aseel/xgoogle/islamicstate/'+news+'.txt', 'r')
	count=0
	for line in f:
   	 d=line.split("http://")
   	 article = Article(url="http://"+d[1])#get the URL
   	 article.download()#Download it
   	 article.parse()#parse the article
   	 title=d[0]
   	 out = open("/Users/Aseel/xgoogle/islamicstate/"+news+"/"+str(count)+".txt", "w")
   	 out.write(title)
   	 out.write(article.text.encode('utf8'))
   	 count=count+1
   	 out.close()
		
	f.close()
