#!/bin/bash

## check disk space ##
diskUse=$(df -H | grep root | awk '{ print $5}' | cut -d'%' -f1 -)

while(($diskUse < 30)) ## limit disk use under 30%
do
  diskUse=$(df -H | grep root | awk '{ print $5}' | cut -d'%' -f1 -)
  echo "Disk Use" $diskUse "%"
  ./apList.sh
  sleep 5    # for command and control
done
