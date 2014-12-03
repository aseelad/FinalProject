## get URL form google serach and write it to a text file
from xgoogle.search import GoogleSearch, SearchError

Newspapers=["champress.net","timesofindia.indiatimes.com", "aawsat.net", "english.people.com.cn" ,"bbc.co.uk" ,"tehrantimes.com"
            ,"dw.de"]
for news in Newspapers:
    
    try:
        gs = GoogleSearch("Gay rights site:"+news)
        gs.results_per_page = 100
        results = []
        while True:
            tmp = gs.get_results()
            if not tmp: # no more results were found
                break
            results.extend(tmp)

        f = open("GayRights/"+news+".txt", "w")
        for res in results:
            f.write(res.title.encode('utf8'))
            f.write(res.url.encode('utf8'))
            f.write("\n")

        f.close()
    except SearchError, e:
      print "Search failed: %s" % e
