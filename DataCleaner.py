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
        match = re.search(regExForDeletingWords,token)
        type(match)
        if match is None:
            ps.stem(token)
            resultTokens.append(token)
    return resultTokens


def SetupDataClean():
    import nltk
    # if there is a problem in downloading nltk data, then run the Install Certificates.command available in your Python folder and then execute the download command
    nltk.download('stopwords')
    #Reference =https://docs.python.org/3/library/re.html


    deleteString = [

        r"""
            (?:
                [:=;] # Eyes
                [oO\-]? # Nose (optional)
                [D\)\]\(\]/\\OpP] # Mouth
            )"""
        ,
        r'<[^>]+>',  # HTML tags
        r'(?:@[\w_]+)',  # @-mentions
        r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
        r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs
        r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
        r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
        r'(?:[\w_]+)',  # other words
        r'(?:\S)',  # anything else
        r'(?<=\D)[.,]|[.,](?=\D)',
        r'<[^>]+>',  # HTML tags
        r'(?:@[\w_]+)',  # @-mentions
        r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
        r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs
        r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
        r'[^\x00-\x7f]'
    ]
    deleteWordsRegEx = re.compile(r'(' + ',' +'.' + '"' + '|'.join(deleteString) + ')', re.VERBOSE | re.IGNORECASE)
    return deleteWordsRegEx


def CombineFiles(fullpath, directory):
    textFile = open(fullpath + "NBA_MSL_NHL_FOOTBALL", "w", encoding="utf-8")
    file_names = os.listdir(directory)
    output = ''
    for file in file_names:
        for  filedata in enumerate(open(file, encoding="utf-8")):
            for line in filedata:
                content = line.strip()
                #output += content + '\t0\n'
                textFile.write(content)
    textFile.close()




def Map(regExForDeletingWords,inputFileName, outputFileName):

    textFile = open(outputFileName,"w", encoding="utf-8")
    #with open(inputFileName, "r", encoding='utf-8') as file:
    for line in enumerate(open(inputFileName, encoding="utf-8")):
            if len(line) == 0:
                continue;
            line = line.strip()
            line = line.lower();
            punctuationToRemove = list(string.punctuation)
            stop = stopwords.words('english') + punctuationToRemove
            new_line = [term for term in tokenize(line,regExForDeletingWords) if not term in stop]
            for word in new_line:
                textFile.write(word + " ")
    textFile.close();

if __name__ == '__main__':

    regEx = SetupDataClean()
    #Map(regEx,"/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/footballText.txt", "/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/CleanedData/CleanedFootballData.txt")
    #Map(regEx,"/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/mlsText.txt", "/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/CleanedData/CleanedMlsData.txt")
    #Map(regEx,"/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/nbaText.txt", "/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/CleanedData/CleanedNbaData.txt")
    #Map(regEx,"/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/mlbText.txt", "/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/CleanedData/CleanedMlbData.txt")
    Map(regEx,"/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/mlbText.txt", "/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/CleanedData/CleanedMlbData.txt")
    #CombineFiles("/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/CleanedData/","/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/CleanedData")
