#!/Users/aman/anaconda3/bin/python
import re
# if there is a problem in downloading nltk data, then run the Install Certificates.command available in your Python folder and then execute the download command
from nltk.corpus import stopwords
import  nltk

import string
from nltk.stem import SnowballStemmer

import sys


def tokenize(text, regExForDeletingWords):

    ps = SnowballStemmer()
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
    # if there is a problem in downloading nltk data, then run the Install Certificates.command available in your Python folder and then execute the download command
    #Reference =https://docs.python.org/3/library/re.html
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

def Map(regExForDeletingWords):

    for line in sys.stdin:
        if len(line) == 0:
            continue;
        line = line.strip()
        line = line.lower();
        punctuationToRemove = list(string.punctuation)
        stop = stopwords.words('english') + punctuationToRemove
        new_line = [term for term in tokenize(line,regExForDeletingWords) if not term in stop]
        for word in new_line:
            print(word.lower() + "\t" + "1")

if __name__ == '__main__':
    regEx = SetupDataClean()
    Map(regEx)
