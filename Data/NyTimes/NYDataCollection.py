import csv
import time
import json
import requests
count = 0
counter = 0
while (1):
    if (count > 50):
        break;
    key1 = 'rdHi9AgUjcjObIPE97DGhv3ArvszGIDM'
    key2 = 'rRYZfvOuDeY6M444'
    url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?api-key='+key1+'&q=football&begin_date=20190101&end_date=20190325&fl=lead_paragraph%2Cabstract%2Cheadline%2Csnippet%2Cweb_url'
    print (" Count : ",count," attempting :",url)
    dataurl = requests.get(url,[])
    data_json = dataurl.json()
    for dest in data_json['response']['docs']:
        if dest == None:
            break;
    f = open("football.txt","a")
    for item in range(len(data_json['response']['docs'])):
            html =data_json['response']['docs'][item]['web_url']
            counter = counter +1
            f.write(str(counter) + "  " + html + "\n")
    f.close()
    dataurl.close()
    count+=1
    time.sleep(10)