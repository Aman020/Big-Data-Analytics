#!/usr/bin/env python
"""mapper.py"""

import sys
<<<<<<< HEAD
myWords = ["football","real","team","madrid","game","match","win","one","first","play","los", "con", "que", "del","win","messi"]
=======
topwords = ["football","real","team","madrid","game","match","win","one","first","play","los", "con", "que", "del"]
tempWord = ""
>>>>>>> 5e544b47aa76ed2eb32fab0ec27402e6d53d38eb
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
<<<<<<< HEAD
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
=======
    # split the line into words
    words = line.split()
    for topword in topwords:
        for i in range(0, len(words)-1):
            if words[i] == topword:
                print("%s|%s\t%s" % (words[i],words[i+1], 1))
>>>>>>> 5e544b47aa76ed2eb32fab0ec27402e6d53d38eb
