#!/bin/bash

directory=$1/ # pick all file in this directory
sDirectory=$directory*
wFile=$directory"wifiList"

echo "$directory"
echo "$sDirectory"
echo "$wFile"

echo "epoch,address,"> ./$wFile

for file in $sDirectory
do
 echo ${file/$directory/}| tr '\n' ','s >> ./$wFile
 less $file | grep Address | awk '{print $5}' | tr '\n' ','s >> ./$wFile
# less $file | grep Signal | awk '{print $3}'| cut -b 7-9 | tr '\n' ','s >> ./$wFile
# less $file | grep ESSID | sed 's/                    ESSID:"//' | sed 's/"//' | tr '\n' ','s >> ./$wFile
 echo '' >> ./$wFile
done

