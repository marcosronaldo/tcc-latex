#!/usr/bin/python
import sys
import os
import csv
import numpy
import operator

HEADER='metric,min,1%,5%,10%,25%,50%,75%,90%,95%,99%,max'
SYSTEM_UNIFIED_PERCENTILS= "/home/marcos/tcc-latex/analise/data/fixed/unified_percentis/"
SYSTEM_APPS_PERCENTILS= "/home/marcos/tcc-latex/analise/apps_data/fixed/unified_percentis/"
# METRICS_LIST=["acc","accm","amloc","dit","lcom4","noc","rfc"]
METRICS_LIST=["acc","accm","amloc","lcom4","dit","rfc"]
SYSTEM_VALUES={"acc":{"75":3.0,"90":12.0,"95":26.0}, 
				"accm":{"75":2.0,"90":4.0,"95":6.0},
				"amloc":{"75":14.0,"90":31.0,"95":55.0},
				"dit":{"75":1.0,"90":2.0,"95":4.0},
				"lcom4":{"75":3.0,"90":7.0,"95":12.0},
				"noc":{"75":0.0,"90":1.0,"95":2.0},
				"rfc":{"75":31.0,"90":85.0,"95":140.0}
				}

# METRICS_WEIGHT={"acc":2,
# 		"accm":2,
# 		"amloc":1,
# 		"dit":1,
# 		"lcom4":2,
# 		"noc":1,
# 		"rfc":2,
# 		"total":11
# 		}
METRICS_WEIGHT={"acc":2,
		"accm":2,
		"amloc":2,
		"dit":1,
		"lcom4":2,
		"rfc":2,
		"total":10
		}


PERCENTIS=["75","90","95"]
PERCENTIS_WEIGHTS={"75":75.0,"90":15.0,"95":5.0}
metrics_file='metrics_percentis.csv'

def get_files_in_path(path):
	files_list = []
	for root, dirs, files in os.walk(path):
		for file in files:
			if file.endswith(".csv"):
				files_list.append(os.path.join(root, file))
	return files_list


def get_limits():
	files = get_files_in_path(SYSTEM_UNIFIED_PERCENTILS)
	limits={}

	for metric_file in files:
		# minimum=[]
		maximum=[]

		with open(metric_file) as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				# minimum.append(row['min'])
				maximum.append(row['75%'])
		metric = os.path.basename(metric_file)[:-4]
		limits[metric]=float(max(maximum))
		# limits[metric]={"min":min(minimum),"max":(float(max(maximum)))}
	return limits

def get_system_apps_percentis():
	files = get_files_in_path(SYSTEM_APPS_PERCENTILS)
	metrics={}

	for metric_file in files:
		metric = os.path.basename(metric_file)[:-4]
		
		with open(metric_file) as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				if row['app'] not in metrics:
					metrics[row['app']]={}
				metrics[row['app']][metric]={"75":row['75%'],"90":row['90%'],"95":row['95%']}
	return metrics

def get_similarity(app_metrics):
	limits = get_limits()
	distances={}
	for app in app_metrics:
		total_distance=0
		print app
		for metric in METRICS_LIST:
			metric_distance=0
			for percentil in PERCENTIS:
				metric_distance+= (abs(float(app_metrics[app][metric][percentil])-SYSTEM_VALUES[metric][percentil])/limits[metric])*PERCENTIS_WEIGHTS[percentil]			
			metric_distance/=95.0			
			metric_distance*=METRICS_WEIGHT[metric]
			print "distance in metric",metric, ":",metric_distance
			total_distance+=metric_distance
		distances[app]=(int(100*(total_distance/float(METRICS_WEIGHT["total"]))))
	return distances

def get_relative_similarity(app_metrics):
	limits = get_limits()
	distances={}
	for app in app_metrics:
		total_distance=0
		print app
		for metric in METRICS_LIST:
			metric_distance=0
			for percentil in PERCENTIS:
				metric_distance+= ((float(app_metrics[app][metric][percentil])-SYSTEM_VALUES[metric][percentil])/limits[metric])*PERCENTIS_WEIGHTS[percentil]			
			metric_distance/=95.0			
			metric_distance*=METRICS_WEIGHT[metric]
			print "distance in metric",metric, ":",metric_distance
			total_distance+=metric_distance
		distances[app]=(int(100*(total_distance/float(METRICS_WEIGHT["total"]))))
	return distances


def mergeTXTfiles(path):

	txtlist = []
	for root, dirs, files in os.walk(path):
		for file in files:
			if file.endswith(".txt"):
				txtlist.append(os.path.join(root, file))

	outfile=path+'/'+metrics_file
	f = open(outfile,'w') #create out file for this metric
	f.write(HEADER+'\n') #write header

	for file in txtlist:
			with open(file,'r') as txt:
				line = txt.read().splitlines()[1].replace(',','.').replace('\t',',')
				f.write(os.path.basename(file)[:-4]+','+line+'\n')
	return outfile

if __name__ == "__main__":	
	# metrics_percentis.csv
	path = sys.argv[1][:-4]
	appname = os.path.basename(sys.argv[1])[:-4]
	outfile = mergeTXTfiles(path)

	metrics={appname:{}}

	with open(outfile) as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				metrics[appname][row['metric']]={"75":row['75%'],"90":row['90%'],"95":row['95%']}

	result = get_relative_similarity(get_system_apps_percentis())
	# print metrics
	print get_relative_similarity(metrics)
	print result	
	l=[]
	for app in result:
		l.append(result[app])
	
	mean=numpy.mean(l)
	std= numpy.std(l)
	print mean
	print std

	sorted_x = sorted(result.items(), key=operator.itemgetter(1))

	with open("result.csv","w") as csvfile:
		for values in sorted_x:
			csvfile.write(values[0]+','+str(values[1])+'\n')

	# for app in result:
	# 	if (result[app] > (mean+std)) or (result[app] < (mean-std)):
	# 		removed[app]=result[app]

	# print removed


	with open("biodyn.csv","w") as csvfile:
		csvfile.write("metric,75%,90%,95%\n")
		for key in metrics:
			for metric in metrics[key]:
				csvfile.write(metric+','+metrics[key][metric]["75"]+','+metrics[key][metric]["90"]+','+metrics[key][metric]["95"]+'\n')