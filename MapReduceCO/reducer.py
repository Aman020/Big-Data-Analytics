#!/usr/bin/env python
"""reducer.py"""
import sys

currentWord = None
currentCount = 0
word = currentWord
wordCoOccur = currentWord

for line in sys.stdin:
    line = line.strip()
    line = line.lower()
    wordCoOccur, count = line.split('\t', 1)
    count = int(count)
    if currentWord == wordCoOccur:
        currentCount = currentCount + count
    else:
        if currentWord:
            print('%s\t%s' % (currentWord, currentCount))
            currentCount = count
        currentWord = wordCoOccur
if currentWord == wordCoOccur:
    print('%s\t%s' % (currentWord, currentCount))


