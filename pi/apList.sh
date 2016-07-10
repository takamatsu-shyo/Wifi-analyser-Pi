#!/bin/bash

## date format ##
NOW=$(date +"%F")
NOWT=$(date +"%s")

## path ##
PATH="./$NOW"

## make a directory ##
if [[ ! -d "$NOW" ]];
then
  /bin/mkdir $NOW
fi

## output ##
/sbin/iwlist wlan0 scan > ./$NOW/$NOWT
