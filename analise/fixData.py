#!/usr/bin/python

import sys
import os

SEPARATOR_COUNT=38

def fixCSV(file):
	originalFile = open(file,'r')
	fixedPath = os.path.dirname(file)+'/fixed/'

	if not os.path.exists(fixedPath):
		os.makedirs(fixedPath)
	fixed = fixedPath+os.path.basename(file)

	fixedFile = open(fixed,'w')
	lineNumber=0

	for line in originalFile:
		lineNumber += 1
		if line.find(', ') is not -1:
			line = line.replace(', ','')
			if (line.count(',')!=SEPARATOR_COUNT):
				print file + ' - error! line ' + str(lineNumber) + ' still need a fix!'
				continue	
		fixedFile.write(line)


if __name__ == "__main__":
    path = sys.argv[1]
    if os.path.isfile(path):
        fixCSV(path)
    else:
        files = [ path + '/' + f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f)) ]
        for f in files:
            fixCSV(f)