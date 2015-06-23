#!/usr/bin/python

import sys
import os

def mergeCSV(files,outfile):
	
	outFile = open(outfile,'w')

	with open(files[0],'r') as f:
		header = f.read().splitlines()[0]# + ',version'
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
	 			outFile.write(line+'\n')#+','+os.path.basename(fileIn)+'\n')					
				
if __name__ == "__main__":
    path = sys.argv[1]
    if os.path.isfile(path):
    	files=[sys.argv[1],sys.argv[2]]
    	outfile =sys.argv[3]
    	mergeCSV(files,outfile)
        # print 'Usage: python mergeMultipleCSV directory outfilename.csv'
    else:
    	filename = sys.argv[2]
        files = [ path + '/' + f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f)) ]
        mergeCSV(files,filename)