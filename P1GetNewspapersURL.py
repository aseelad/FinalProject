##part 1
# Get the google search results.
##return the URLs
from google import search

search_term="islamic state"
Newspapers=["champress.net","timesofindia.indiatimes.com", "aawsat.net", "english.people.com.cn" ,"bbc.co.uk" ,"tehrantimes.com"
            ,"dw.de"]
for news in Newspapers:
    gs = search_term+" site:"+news
    f = open("/Users/Aseel/FinalProject/"+search_term+"/"+news+".txt", "w")
    for url in search(gs, num=100, stop=1000):
		f.write(url)
		f.write("\n")

    f.close()