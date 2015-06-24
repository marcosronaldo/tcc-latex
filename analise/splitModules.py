#!/usr/bin/python

import sys
import os

def splitModules(files):

	basedir = os.path.dirname(files[0])

	for file in files:

		#diretorio para salvar um csv pra cada pacote
		newfolder = os.path.basename(file)
		newfolder = newfolder[:-4]
		newdir=basedir+'/'+newfolder+"_splited"
		if not os.path.exists(newdir):
			os.makedirs(newdir)

		packages = fileToDict(file)

		header = ""
		with open(file,'r') as f:
			header=f.read().splitlines()[0]

		for key in packages:
			with open(newdir+"/"+key+".csv",'w') as out:
				out.write(header+"\n")
				for line in packages[key]:
					out.write(line)
		
def fileToDict(file):
	packages={}
	with open(file,'r') as f:
		# packages["FILE_HEADER"] = f.read().splitlines()[0]
		#para cada linha do arquivo
		firstLine=True
		for line in f:
			if firstLine:
				firstLine=False
				continue
			package=""
			module = line.split(",")[1].split("::")
			del module[-1]
			for piece in module:
				if not package:
					package=piece
				else:
					package=package+"::"+piece
			if package not in packages:
				packages[package]=[]
			packages[package].append(line)
	return packages

if __name__ == "__main__":
    path = sys.argv[1]
    if os.path.isfile(path):
    	splitModules([path])
    else:
        files = [ path + '/' + f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f)) ]
        splitModules(files)