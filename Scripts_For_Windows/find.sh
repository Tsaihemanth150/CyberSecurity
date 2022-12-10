echo "The Details of the internet-connectivity:--"
ipconfig

echo "The ARP entry tables :--"
arp -a

echo "Find out the route of the routing for "
read input
tracert $input >> output.txt ## the output is stored in the file.



## please check the output file in pwd(present working directorty).

 # the shot script to find the basic details like internet connectivity, ARP Table, and Routing route;
