#!/bin/bash

echo "Please choose the desired option:"

echo "1. View System information"
echo "2. View System information with output in textfile "
echo "3. Lists All Installed Drivers "
echo "4. View all PC’s Environment Variables "
echo "5. View all the list of process running now "

read num


if [[ $num -eq 1 ]]
then
    systeminfo
elif [[ $num -eq  2 ]]
then
   systeminfo >> output.txt
elif [[ $num -eq  3 ]]
then
   driverquery
elif [[ $num -eq  4 ]]
then
   set
else 
 tasklist
fi
