#!/bin/bash

Rscript loop_percentis.R /home/marcos/biodyn/biodynapp/biodyn-details.csv
python normalize.py /home/marcos/biodyn/biodynapp/biodyn-details.csv
