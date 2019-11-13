#!/bin/bash
. /opt/linuxer/etc/client.conf
. /opt/linuxer/lib/client.lib

CHOICE=9

while [ ! $CHOICE -eq 0 ]
do

echo "This is the client of Linuxer for student. (V4.0)"
echo "MENU"
echo "  1 Start experiment environment (Press Ctl+c to stop)"
echo "  2 Submit your experiment result"
echo "  3 Connect to the server of linuxer"
echo "  0 EXIT"
echo "Please input your choice:"

read CHOICE


case $CHOICE in
  1) start ./labs/;;
  2) submit localhost;;
  3) server localhost;;
  *) CHOICE=0
esac

done

