#!/usr/bin/python

import sys
import os

OUT_FILENAME='all_merged.csv'

def mergeCSV(files):
	
	outPath = os.path.dirname(files[0])
	outFilePath = outPath+'/'+OUT_FILENAME
	outFile = open(outFilePath,'w')

	with open(files[0],'r') as f:
		header = f.read().splitlines()[0] + ',version'
		outFile.write(header+'\n')

	print 'header written!'

	for fileIn in files:
		print 'appending file ' + os.path.basename(fileIn) +'...'
		with open(fileIn,'r') as f:
			count=0
			for line in f.read().splitlines():
				if count==0:
					count=1
					continue # skip header/first line
	 			outFile.write(line+','+os.path.basename(fileIn)+'\n')					
				
if __name__ == "__main__":
    path = sys.argv[1]
    if os.path.isfile(path):
        print 'this script needs to receive a directory!'
    else:
        files = [ path + '/' + f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f)) ]
        mergeCSV(files)