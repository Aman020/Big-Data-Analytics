from bs4 import BeautifulSoup
import requests

textFile = open("FotballText.txt","wb")
temp = open("football.txt", "r")

with open("football.txt", "r") as f:
    try:

        for htmlLink in f:
            print(htmlLink)
            page =requests.get(htmlLink.split("  ")[1])

            data = page.text
            soup = BeautifulSoup(data, 'html.parser')
            for article in soup.find_all('article'):
                for para in article.find_all('p'):
                    textFile.write(para.get_text().encode('utf-8'))
    except:
        textFile.close()
