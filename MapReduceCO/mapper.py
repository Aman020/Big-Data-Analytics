#!/usr/bin/env python
"""mapper.py"""

import sys
myWords = ["football","real","team","madrid","game","match","win","one","first","play","los", "con", "que", "del","win","messi"]
for line in sys.stdin:
    if len(line) == 0:
        continue;
    line = line.strip()
    line = line.lower();
    wordsDict = {}
    for word in line:
        if word in myWords:
            wordsDict[word] = True
    for loc,word in enumerate(myWords):
        if word not in wordsDict:
            continue;
        for i2 in range(loc+1,len(myWords)):
            if myWords[i2] not in wordsDict:
                continue;
            print (myWords[loc]+","+myWords[i2]+"\t1")
