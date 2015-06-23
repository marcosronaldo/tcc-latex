#!/bin/bash
BASEDIR=~/tcc-latex/analise/data/fixed/unified_percentis
APPS_BASEDIR=~/tcc-latex/analise/apps_data/fixed/unified_percentis
OUTDIR=~/tcc-latex/tables

metrics_list="accm amloc cbo dit lcom4 loc noc rfc"
extension=".csv"
android="_android.tex"
apps="_apps.tex"

for metric in $metrics_list
do
	android_file=$OUTDIR/$metric$android
	apps_file=$OUTDIR/$metric$apps

	csv2latex $BASEDIR/$metric$extension > $android_file
	csv2latex $APPS_BASEDIR/$metric$extension > $apps_file

	head -n -1 $android_file > temp.txt
	mv temp.txt $android_file

	tail -n +5 $android_file > temp.txt
	mv temp.txt $android_file

	head -n -1 $apps_file > temp.txt
	mv temp.txt $apps_file

	tail -n +5 $apps_file > temp.txt
	mv temp.txt $apps_file

done