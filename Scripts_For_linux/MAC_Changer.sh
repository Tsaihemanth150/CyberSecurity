#!/bin/bash

echo "enter MAC"
read mac
ifconfig etho down
ifconfig etho hw ether $mac
ifconfig etho up

ifconfig etho down
ifconfig etho hw ether $mac
ifconfig etho up
ifconfig 


#Use command for executable permission : chmod +X MAC_Changer.sh
#To run script : ./MAC_Changer.sh
