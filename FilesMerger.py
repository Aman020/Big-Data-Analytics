import sys
import glob
import errno

outputFile = open("/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/NyTimes/Scrapped Data/MergedData.txt","w+")
path = '/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/NyTimes/Scrapped Data/*.txt'
files = glob.glob(path)
for name in files: # 'file' is a builtin type, 'name' is a less-ambiguous variable name.
    try:
        with open(name) as f: # No need to specify 'r': this is the default.
            outputFile.write(f.read())
    except IOError as exc:
        if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
            raise # Propagate other kinds of IOError.