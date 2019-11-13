#!/bin/bash
. /opt/linuxer/etc/server.conf
. /opt/linuxer/lib/server.lib

#TERM=linux
CHOICE=9
#clear

while [ ! $CHOICE -eq 0 ]
do

echo "Student function."
echo "MENU"
echo "  1 Change passwd"
echo "  2 Check score" 
echo "  0 Return"
echo "Please input your choice:"

read CHOICE


case $CHOICE in
  1) passwd;;
  2) checkscore;;
  *) CHOICE=0
esac

done

