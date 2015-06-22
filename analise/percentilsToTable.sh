#!/bin/bash
BASEDIR=~/tcc-latex/analise/data/fixed/unified_percentils
APPS_BASEDIR=~/tcc-latex/analise/apps_data/fixed/unified_percentils
OUTDIR=~/tcc-latex/tables

metrics_list="accm amloc cbo dit lcom4 loc noc rfc"
extension=".csv"
android="_android.tex"
apps="_apps.tex"

for metric in $metrics_list
do
	csv2latex $BASEDIR/$metric$extension >> $OUTDIR/$metric$android
	csv2latex $APPS_BASEDIR/$metric$extension >> $OUTDIR/$metric$apps
done
