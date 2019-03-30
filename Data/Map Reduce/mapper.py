
from nltk.tokenize import word_tokenize
import re
import pandas as pd
from nltk.corpus import stopwords
import string
from nltk.stem import PorterStemmer



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
    deleteString = [
        r"""
            (?:
                [:=;] # Eyes
                [oO\-]? # Nose (optional)
                [D\)\]\(\]/\\OpP] # Mouth
            )"""
        ,
        r'(?<=\D)[.,]|[.,](?=\D)',
        r'<[^>]+>',  # HTML tags
        r'(?:@[\w_]+)',  # @-mentions
        r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
        r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs
        r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
        r'[^\x00-\x7f]'
    ]
    deleteWordsRegEx = re.compile(r'(' + ',' +'.' + '|'.join(deleteString) + ')', re.VERBOSE | re.IGNORECASE)
    return deleteWordsRegEx


def CleanData(inputFile, outputFile, regEx):
    output = open(outputFile, "w+")
    data = pd.read_csv(inputFile)
    punctuationToRemove = list(string.punctuation)
    stop = stopwords.words('english') + punctuationToRemove
    for tweet in data.text:
        line =' '.join([term for term in tokenize(tweet, regEx) if term not in stop])
        output.write(line)
    output.close()
    print('Cleaned data saved at ' , outputFile)

if __name__ == '__main__':
    regEx = SetupDataClean()
    CleanData(inputFile="/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/twitterdata.csv",outputFile="/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/cleanedTwitterData.txt", regEx=regEx)
