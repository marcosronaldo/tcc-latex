#!/bin/bash
TABLE_OUTDIR=~/tcc-latex/tables
TABLE_FILE=relative_distance.tex

Rscript loop_percentis.R /home/marcos/biodyn/biodynapp/biodyn-details.csv
python api_distance.py /home/marcos/biodyn/biodynapp/biodyn-details.csv

tex_table=$TABLE_OUTDIR/$TABLE_FILE

csv2latex result.csv > $tex_table

head -n -1 $tex_table > temp.txt
mv temp.txt $tex_table

tail -n +5 $tex_table > temp.txt
mv temp.txt $tex_table
