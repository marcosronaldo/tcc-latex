#!/bin/bash

BASEDIR=~/tcc-latex/analise/data/fixed/unified_percentis
APPS_BASEDIR=~/tcc-latex/analise/apps_data/fixed/unified_percentis

metrics_list="accm amloc cbo dit lcom4 loc noc rfc"

echo "removing fixed folder with old android files..."
rm -rf ~/tcc-latex/analise/data/fixed/
echo "removing extra commas from CSV files..."
python fixData.py ~/tcc-latex/analise/data/
echo "generating percentis..."
Rscript script-loop-percentis.R
echo "unifying percentis for all android versions..."
python ~/tcc-latex/analise/unifyPercentis.py ~/tcc-latex/analise/data/fixed/ 

echo "__"

echo "removing fixed folder with old app files..."
rm -rf ~/tcc-latex/analise/apps_data/fixed/
echo "removing extra commas from CSV files..."
python fixData.py ~/tcc-latex/analise/apps_data/
echo "generating percentis..."
Rscript loop_percentis_apps.R
echo "unifying percentis for all android versions..."
python ~/tcc-latex/analise/unifyPercentisApps.py ~/tcc-latex/analise/apps_data/fixed/

echo "__"

echo "unifying all percentis for android and apps in same directory"
globalpercentis=~/tcc-latex/analise/global_percentis
mkdir $globalpercentis
extension=".csv"
for metric in $metrics_list
do
	fname=$metric$extension
	python mergeMultipleCSV.py $BASEDIR/$fname $APPS_BASEDIR/$fname $globalpercentis/$fname
done

# echo "parsing all unified percentil tables to use in latex..."
# sh ~/tcc-latex/analise/percentisToTable.sh

echo "ploting line graphs with each metric and number of classes..."
Rscript plotMetricXNumberOfClasses.R 

echo "DONE!"