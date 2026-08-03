#!/bin/bash

#As a Linux System Administrator, you want to 
#prevent server crashes caused by running out of 
#disk space. You need to write a Bash script that 
#automatically inspects disk usage and takes action 
#based on the occupation level.

percentage=$(df -h / | tr -s " " "," | cut -d "," -f 5 | grep -o '[0-9]\+')
date=$(date +%Y-%m-%d)


if [ "$percentage" -ge "80" ];
then
        echo -e "DISK ALERT!\nThe disk is $percentage% in USE."

        echo "[$date] - Disk Usage: $percentage% - Status: CRITICAL" >> "./disco.log"

else
        echo "The storage is helthy with $percentage% in use."
        echo "[$date] - Disk Usage: $percentage% - Status: OK" >> "./disco.log"

fi
