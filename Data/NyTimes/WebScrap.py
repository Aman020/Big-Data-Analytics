from bs4 import BeautifulSoup
import requests


def ScrapData(inputFileName, outputFileName):

    textFile = open(outputFileName,"wb")
    with open(inputFileName, "r") as f:
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
if __name__ == '__main__':
    ScrapData(inputFileName="football.txt", outputFileName="FotballPlainText.txt")
