echo "Hide your data form others to catch it!!!!"


echo "1.IF you want to hide your folder"
echo "2. IF you want to un-hide your folder"
echo "please enter your option"

read num


if [[ $num -eq 1 ]]
then
	echo "please enter folder name to hide it"
	read hide
	attrib +h +s +r $hide

else
	echo "please enter folder name to un-hide it"
	read unhide
	attrib -h -s -r $hide
fi