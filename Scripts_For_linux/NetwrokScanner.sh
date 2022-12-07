#!/bin/bash

echo "Enter your IP"
read IP

echo "Enter Port "
read port

echo "Select a Scan \n 1 for Aggresive \n 2 for Syn \n 3 for TCP "
read temp

if [ $temp -eq 1 ]
then
   nmap -A $IP -p $port | grep open
elif[$temp -eq 2 ]
then
   nmap -sS -0 -sV $IP -p $port | grep open
elif[$temp -eq 3]
then
   nmap -sT -0 -sV $IP -p $port | grep open
fi
