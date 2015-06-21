#!/usr/bin/python
import sys
import os

OUT_FILENAME='all_merged.csv'
TXT_METRICS=['acc.txt','accm.txt','amloc.txt','an.txt','anpm.txt',
		 'asom.txt','auv.txt','bd.txt','bf.txt','cbo.txt',
		 'da.txt','dbz.txt','df.txt','dit.txt','dnp.txt',
		 'dupv.txt','fgbo.txt','lcom4.txt','loc.txt','mlk.txt',
		 'mmloc.txt','noa.txt','noc.txt','nom.txt','npa.txt',
		 'npm.txt','obaa.txt', 'osf.txt', 'pitfc.txt','rfc.txt',
		 'rogu.txt','rsva.txt','saigv.txt', 'sc.txt','ua.txt',
		 'uaf.txt', 'uav.txt']
VERSIONS=['android-1.6_r1.2','android-1.6_r1.5',
          'android-2.0_r1','android-2.1_r2.1p2',
          'android-2.2_r1','android-2.2.3_r2',
          'android-2.3_r1','android-2.3.7_r1',
          'android-4.0.1_r1','android-4.0.4_r2.1']

HEADER='version,min,1%,5%,10%,25%,50%,75%,90%,95%,99%,max'
OUT_FOLDER='unified_percentils'

def mergeTXTfiles(files, path):

	if not os.path.exists(path+'/'+OUT_FOLDER):
		os.makedirs(path+'/'+OUT_FOLDER)

	for metric in TXT_METRICS:
		outfile=path+'/'+OUT_FOLDER+'/'+metric[:-4]+'_full'+'.csv'
		f = open(outfile,'w') #create out file for this metric
		f.write(HEADER+'\n') #write header

		for version in VERSIONS:
			for file in files:
				if((os.path.basename(file) == metric) and
					(os.path.basename(os.path.dirname(file)) == version)):
					with open(file,'r') as txt:
						f.write(version+','+txt.read().splitlines()[1].replace(',','.').replace('\t',',')+'\n')

if __name__ == "__main__":
    path = sys.argv[1]
    if os.path.isfile(path):
        print 'this script needs to receive a directory!'
    else:
		txtlist = []
		for root, dirs, files in os.walk(path):
			for file in files:
				if file.endswith(".txt"):
					txtlist.append(os.path.join(root, file))
		mergeTXTfiles(txtlist, path)
		        