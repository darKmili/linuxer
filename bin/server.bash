#!/bin/bash
. /opt/linuxer/etc/server.conf
. /opt/linuxer/lib/server.lib

CHOICE=9

clear

while [ ! $CHOICE -eq 0 ]
do

echo "This is the server of Linuxer. (V4.0)"
echo "MENU"
echo "  1 Register a new account"
echo "  2 Functions" 
echo "  0 Return"
echo "Please input your choice:"

read CHOICE


case $CHOICE in
  1) register;;
  2) (read -p "ID:" ID && su $ID);;
  *) CHOICE=0
esac

done

