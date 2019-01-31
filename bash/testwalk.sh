#!/bin/bash
	while true; do
		iwconfig wlan0|grep -i "Access Point"|cut -c60-76
		sleep 1
	done
