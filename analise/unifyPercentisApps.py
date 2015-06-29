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

TXT_METRICS=['acc.txt','accm.txt','amloc.txt','cbo.txt',
		 'dit.txt','lcom4.txt','loc.txt','noc.txt','nom.txt','rfc.txt']

HEADER='app,classes,min,1%,5%,10%,25%,50%,75%,90%,95%,99%,max'
OUT_FOLDER='unified_percentis'

def listapps(path):
	csvlist = []
	for root, dirs, files in os.walk(path):
		for file in files:
			if file.endswith(".csv"):
				csvlist.append(os.path.basename(file).replace("-details.csv",""))
	return csvlist

def classesapps(path):
	csvlist = {}
	for root, dirs, files in os.walk(path):
		for file in files:
			if file.endswith(".csv"):
				csvlist[os.path.basename(file).replace("-details.csv","")]=sum(1 for line in open(os.path.join(root, file)))
	return csvlist

def mergeTXTfiles(files, path, appslist):

	number_of_classes=classesapps(path)

	if not os.path.exists(path+'/'+OUT_FOLDER):
		os.makedirs(path+'/'+OUT_FOLDER)

	for metric in TXT_METRICS:
		outfile=path+'/'+OUT_FOLDER+'/'+metric[:-4]+'.csv'
		f = open(outfile,'w') #create out file for this metric
		f.write(HEADER+'\n') #write header
		for app in appslist:
			for file in files:
				if((os.path.basename(file) == metric) and
					(os.path.basename(os.path.dirname(file)) == (app+"-details"))):
					with open(file,'r') as txt:
						line = round_csv_values(txt.read().splitlines()[1].replace(',','.').replace('\t',','),2)
						f.write(app+','+str(number_of_classes[app]) +','+line+'\n')

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
		mergeTXTfiles(txtlist, path, listapps(path))
		        