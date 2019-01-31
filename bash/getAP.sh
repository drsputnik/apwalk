#!/bin/bash
iwconfig wlan0|grep -i "Access Point"|cut -c60-76
