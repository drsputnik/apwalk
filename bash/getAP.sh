##!/bin/bash
ifconfig wlan0 down
ifconfig wlan0 up
sleep 1
iw wlan0 station dump|grep Station|cut -c9-25
iw wlan0 station dump|grep signal|cut -c12-|cut -d ' ' -f 1

