#!/bin/bash
sudo rm -rf /etc/X11/xorg.conf.d/40-libinput.conf
sudo mkdir /etc/X11/xorg.conf.d
sudo cp ./usr/tft35a-overlay.dtb /boot/overlays/
sudo cp ./usr/tft35a-overlay.dtb /boot/overlays/tft35a.dtbo
sudo cp -rf ./usr/99-calibration.conf-35  /etc/X11/xorg.conf.d/99-calibration.conf
sudo cp -rf ./usr/99-fbturbo.conf  /usr/share/X11/xorg.conf.d/
if [ -b /dev/mmcblk0p7 ]; then
sudo cp ./usr/cmdline.txt-noobs /boot/cmdline.txt
else
sudo cp ./usr/cmdline.txt /boot/
fi
sudo cp ./usr/inittab /etc/
sudo cp ./boot/config-35.txt /boot/config.txt
nodeplatform=`uname -n`
kernel=`uname -r`
version=`uname -v`
if test "$nodeplatform" = "raspberrypi";then
echo "this is raspberrypi kernel"
version=${version%% *}
version=${version#*#}
echo $version
if test $version -lt 970;then
echo "reboot"
else
echo "need to update touch configuration"
if test $version -ge 1023;then
echo "install xserver-xorg-input-evdev_2.10.5-1"
sudo dpkg -i -B xserver-xorg-input-evdev_2.10.5-1_armhf.deb
else
echo "install xserver-xorg-input-evdev_1%3a2.10.3-1"
sudo dpkg -i -B xserver-xorg-input-evdev_1%3a2.10.3-1_armhf.deb
fi
sudo cp -rf /usr/share/X11/xorg.conf.d/10-evdev.conf /usr/share/X11/xorg.conf.d/45-evdev.conf
echo "reboot"
fi
else
echo "this is not raspberrypi kernel, no need to update touch configure, reboot"
fi

