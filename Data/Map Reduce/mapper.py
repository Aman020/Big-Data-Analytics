
from nltk.tokenize import word_tokenize
import re
import pandas as pd
from nltk.corpus import stopwords
import string
from nltk.stem import PorterStemmer


ps = PorterStemmer()
import nltk
# if there is a problem in downloading nltk data, then run the Install Certificates.command available in your Python folder and then execute the download command
nltk.download('stopwords')
f = open("/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/cleanedTwitterData.txt", "w+")


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


def tokenize(text):
    resultTokens = []
    tokens = [t for t in text.split()]
    for token in tokens:
        match = re.search(deleteWordsRegEx,token)
        type(match)
        if match is None:
            ps.stem(token)
            resultTokens.append(token)
    return resultTokens

data = pd.read_csv("/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/twitterdata.csv")
punctuationToRemove = list(string.punctuation)
stop = stopwords.words('english') + punctuationToRemove
for tweet in data.text:
    line =' '.join([term for term in tokenize(tweet) if term not in stop])

    f.write(line)

f.close()
