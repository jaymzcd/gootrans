#!/usr/bin/env sh

# Simple shell script to read a file and translate each line
# using the python file
while read line
do
    ../gootrans/translate.py "$line"
done < titles.txt

