#!/usr/bin/python

import re
# if there is a problem in downloading nltk data, then run the Install Certificates.command available in your Python folder and then execute the download command
from nltk.corpus import stopwords
import string
from nltk.stem import PorterStemmer
import os



def tokenize(text, regExForDeletingWords):
    ps = PorterStemmer()
    resultTokens = []
    tokens = [t for t in text.split()]
    for token in tokens:
        # match = re.sub(r'([^\s\w]|_)+', '', token)
        # type(match)
        # if match is None:
        if token.isalpha():
            ps.stem(token)
            resultTokens.append(token)
    return resultTokens


def SetupDataClean():
    import nltk
    # if there is a problem in downloading nltk data, then run the Install Certificates.command available in your Python folder and then execute the download command
    nltk.download('stopwords')
    #Reference =https://docs.python.org/3/library/re.html
    deleteString = [ ]
    deleteWordsRegEx = re.compile(r'(' + ',' +'.' + '"' + '|'.join(deleteString) + ')', re.VERBOSE | re.IGNORECASE)
    return deleteWordsRegEx



def Map(regExForDeletingWords,inputFileName, outputFileName):

    textFile = open(outputFileName,"w", encoding="utf-8")
    #with open(inputFileName, "r", encoding='utf-8') as file:
    for filelineno, line in enumerate(open(inputFileName, encoding="utf-8")):
            if len(line) == 0:
                continue;
            line = line.strip()
            #line = line.lower();
            #punctuationToRemove = list(string.punctuation)
            stop = stopwords.words('english') #+ punctuationToRemove
            new_line = [term for term in tokenize(line,regExForDeletingWords) if not term in stop]
            for word in new_line:
                textFile.write(word + " ")
    textFile.close();

if __name__ == '__main__':

    regEx = SetupDataClean()
    #Map(regEx,"/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/footballText.txt", "/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/CleanedData/CleanedFootballData.txt")
    Map(regEx,"/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/mlsText.txt", "/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/CleanedData/CleanedMlsData.txt")
    Map(regEx,"/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/nbaText.txt", "/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/CleanedData/CleanedNbaData.txt")
    Map(regEx,"/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/nhlText.txt", "/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/CleanedData/CleanedNhlData.txt")
    Map(regEx, "/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/mlbText.txt","/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/CleanedData/CleanedMlbData.txt")
