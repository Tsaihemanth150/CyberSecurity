#!/bin/bash

echo "Please choose the desired option:"

echo "1. Find the Route to the website or ip"
echo "2. Find the Route to the website or ip and save output in text file "
echo "3. check the Host/IP is UP/Down "
echo "4. check the Host/IP is UP/Down store output in text file "

read num


if [[ $num -eq 1 ]]
then
   echo "Enter the website adress or ip " 
     read webip
     tracert $webip
elif [[ $num -eq  2 ]]
then
  echo "Enter the website adress or ip " 
   read webip
    tracert $webip >> output.txt
elif [[ $num -eq  3 ]]
then
   echo "check the Host/IP is UP/Down " 
    read webip
     ping $webip
else 
echo "check the Host/IP is UP/Down "
read webip
  ping $webip >>output.txt
fi
