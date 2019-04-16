#!/usr/bin/python
import sys

wordCountDict = {}
for line in sys.stdin:
    line = line.strip()
    lineTokens = line.split('\t')
    word,count = lineTokens[0],lineTokens[1]
    if word in wordCountDict:
        wordCountDict[word] += 1
    else:
        wordCountDict[word] = int(count)
for word in wordCountDict.keys():
    print(word + "\t" +  wordCountDict[word])