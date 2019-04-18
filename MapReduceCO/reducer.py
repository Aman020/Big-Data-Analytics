#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter

import sys

curr_word = ""
curr_count = 0
word = curr_word
wordpair = curr_word

for line in sys.stdin:
    line = line.strip()
<<<<<<< HEAD
<<<<<<< HEAD
    lt =  line.split('\t')
    if len(lt)!=2:
        continue;
    word,count = lt[0],lt[1]
    count = int(count)
    if prev_word == None:
        prev_word = word
=======
=======
>>>>>>> 5e544b47aa76ed2eb32fab0ec27402e6d53d38eb
    wordpair, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
<<<<<<< HEAD
>>>>>>> 5e544b47aa76ed2eb32fab0ec27402e6d53d38eb
=======
>>>>>>> 5e544b47aa76ed2eb32fab0ec27402e6d53d38eb
        continue
    if curr_word == wordpair:
        curr_count += count
    else:
        if curr_word:
            # write result to STDOUT
            print('%s\t%s' % (curr_word, curr_count))
        curr_count = count
        curr_word = wordpair

if curr_word == wordpair:
    print('%s\t%s' % (curr_word, curr_count))