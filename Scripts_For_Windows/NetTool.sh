#!/bin/bash
echo "Welcome to the NetTool"
echo "Here what you can dop with this:"
echo "1.Find the Hostname"
echo "2.Find overview of all the network connections in the device"
echo "3.Check your routing table "
echo "4.Loose source route along host-list."
echo "5.find path to the ip or domain"

read num 

if [[ $num -eq 1 ]]
then
  hostname

elif [[ $num -eq 2 ]]
then
  netstat

elif [[$num -eq 3]]
then
	route print

elif [[ $num -eq 4 ]]
then
	echo "Enter the ip or domain name"
	read id
	pathping -g $id

else 
	echo "Entere domain or ip adress to find path"
	read dm
 	pathping -q 10 $dm
fi
