echo "The Details of the internet-connectivity:--"
ipconfig

echo "The ARP entry tables :--"
arp -a

echo "Find out the route of the routing for "
read input
tracert $input


 # the shot script to find the basic details like internet connectivity, ARP Table, and Routing route;
