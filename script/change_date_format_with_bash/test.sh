#!/bin/bash

echo "============================================"
FILE=./sample_date1.csv
cat $FILE
echo " => change to the followings"
awk 'BEGIN{FS=OFS="|"} NR>1 \
    {cmd = "date -d \"" $2 "\" \"+%Y-%m-%d\"";
    cmd | getline out; 
    $2=out; 
    print $0}' $FILE

echo "============================================"
FILE=./sample_date2.csv
cat $FILE
echo " => change to the followings"
awk 'BEGIN{FS=OFS="|"} NR>1 \
    {cmd = "date -d \"" $2 "\" \"+%Y/%m/%d\"";
    cmd | getline out; 
    $2=out; 
    print $0}' $FILE
echo "============================================"

#close("uuidgen")} 1' ./sample_date.csv

