##!/bin/bash
iwconfig wlan0|grep -i "Access Point"|cut -c60-76
iw wlan0 station dump|grep signal|cut -c12-

