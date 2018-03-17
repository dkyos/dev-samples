#!/bin/bash

echo "============================================"
FILE=$1
echo " => change to the followings"
awk 'BEGIN{FS=OFS="|"} NR>1 \
    {cmd = "date -d \"" $20 "\" \"+%Y/%m/%d\"";
    cmd | getline out; 
    $20=out; 
    print $0}' $FILE

#close("uuidgen")} 1' ./sample_date.csv

