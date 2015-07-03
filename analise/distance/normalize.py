#!/usr/bin/python
import sys
import os
import csv

SYSTEM_UNIFIED_PERCENTILS= "/home/marcos/tcc-latex/analise/data/fixed/unified_percentis/"
SYSTEM_APPS_PERCENTILS= "/home/marcos/tcc-latex/analise/apps_data/fixed/unified_percentis/"
# METRICS_LIST=["acc","accm","amloc","cbo","dit","lcom4","loc","noc","rfc"]

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
		minimum=[]
		maximum=[]

		with open(metric_file) as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				minimum.append(row['min'])
				maximum.append(row['max'])
		metric = os.path.basename(metric_file)[:-4]
		limits[metric]={"min":min(minimum),"max":max(maximum)}
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

def get_distance(app_metrics):
	pass


if __name__ == "__main__":
	limits = get_limits()
	print get_system_apps_percentis()

	