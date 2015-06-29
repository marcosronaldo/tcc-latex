#!/usr/bin/python
import sys
import os

# TXT_METRICS=['acc.txt','accm.txt','amloc.txt','an.txt','anpm.txt',
# 		 'asom.txt','auv.txt','bd.txt','bf.txt','cbo.txt',
# 		 'da.txt','dbz.txt','df.txt','dit.txt','dnp.txt',
# 		 'dupv.txt','fgbo.txt','lcom4.txt','loc.txt','mlk.txt',
# 		 'mmloc.txt','noa.txt','noc.txt','nom.txt','npa.txt',
# 		 'npm.txt','obaa.txt', 'osf.txt', 'pitfc.txt','rfc.txt',
# 		 'rogu.txt','rsva.txt','saigv.txt', 'sc.txt','ua.txt',
# 		 'uaf.txt', 'uav.txt']

TXT_METRICS=['accm.txt','amloc.txt','cbo.txt',
		 'dit.txt','lcom4.txt','loc.txt','noc.txt','nom.txt',
		 'rfc.txt']


VERSIONS=['android-1.6_r1.2','android-1.6_r1.5',
          'android-2.0_r1','android-2.1_r2.1p2',
          'android-2.2_r1','android-2.2.3_r2',
          'android-2.3_r1','android-2.3.7_r1',
          'android-4.0.1_r1','android-4.0.4_r2.1',
          'android-4.1.1_r1', 'android-4.3.1_r1',
          'android-5.1.0_r1',]

NUMBER_OF_CLASSES={'android-1.6_r1.2':5745,
				  'android-1.6_r1.5':5745,
				  'android-2.0_r1':6331,
				  'android-2.1_r2.1p2':6360,
				  'android-2.2_r1':7352,
				  'android-2.2.3_r2':7358,
          		  'android-2.3_r1':8093,
          		  'android-2.3.7_r1':8240,
          		  'android-4.0.1_r1':11709,
          		  'android-4.0.4_r2.1':11851,
          		  'android-4.1.1_r1':14115,
          		  'android-4.3.1_r1':15472,
          		  'android-5.1.0_r1':20129,
				}   

HEADER='version,classes,min,1%,5%,10%,25%,50%,75%,90%,95%,99%,max'
OUT_FOLDER='unified_percentis'

def mergeTXTfiles(files, path):

	if not os.path.exists(path+'/'+OUT_FOLDER):
		os.makedirs(path+'/'+OUT_FOLDER)

	for metric in TXT_METRICS:
		outfile=path+'/'+OUT_FOLDER+'/'+metric[:-4]+'.csv'
		f = open(outfile,'w') #create out file for this metric
		f.write(HEADER+'\n') #write header

		for version in VERSIONS:
			for file in files:
				if((os.path.basename(file) == metric) and
					(os.path.basename(os.path.dirname(file)) == version)):
					with open(file,'r') as txt:
						line = round_csv_values(txt.read().splitlines()[1].replace(',','.').replace('\t',','),2)
						f.write(version+','+str(NUMBER_OF_CLASSES[version])+','+line+'\n')

def round_csv_values(line,decimals):
	values = line.split(",")
	newLine=""
	for value in values:
		number= num(value)
		if not newLine:
			newLine=str(number)
		else:
			newLine=newLine+","+str(number)
	return newLine

def num(string):
	try:
		return int(string)
	except ValueError:
		return round(float(string),2)

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
		        