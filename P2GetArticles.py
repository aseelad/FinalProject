##P2
## read URL from text file and get the article text 


import newspaper
from newspaper import Article

Newspapers=["champress.net", "english.people.com.cn" ,"bbc.co.uk" ,"tehrantimes.com","dw.de"]
      
search_term="Gay Rights"
      
for news in Newspapers:
	f = open("/Users/Aseel/FinalProject/GayRights/"+news+".txt", 'r')
	count=0
	for line in f:
		##d=line.split("http://")
   	 	article = Article(line)#get the URL
   	 	article.download()#Download it
   	 	article.parse()#parse the article
   	 	##title=d[0]
   	 	out = open("/Users/Aseel/FinalProject/GayRights/"+news+"/"+str(count)+".txt", "w")
   	 	##out.write(title)
   	 	out.write(article.text.encode('utf8'))
   	 	count=count+1
   	 	out.close()
		
	f.close()
