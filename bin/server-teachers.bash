#!/bin/bash
. /opt/linuxer/etc/server.conf
. /opt/linuxer/lib/server.lib

CHOICE=9
clear
while [ ! $CHOICE -eq 0 ]
do

echo "Teacher functions."
echo "MENU"
echo "  1 Change passwd"
echo "  2 List scores"
echo "  3 Mark reports"
echo "  4 Analyze experiments(TODO)"
echo "  5 System admin(TODO)" 
echo "  0 Return"
echo "Please input your choice:"

read CHOICE


case $CHOICE in
  1) passwd;;
  2) listscore;;
  3) mark;;
  4) python3 run.py;;
  5) todo admin;;
  *) CHOICE=0
esac

done

