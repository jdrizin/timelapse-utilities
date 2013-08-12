#!/bin/bash

portstring=$(gphoto2 --auto-detect |egrep -o "usb:...,...")
port1=$(echo $portstring | head -n1)
port2=$(echo $portstring | tail -n1)
command="--capture-image-and-download"
frames="-F 1440"
interval="-I 5"

camera1=`gphoto2 --port $port1 --get-config ownername |grep Current|sed -e 's/Current:\ //'`
camera2=`gphoto2 --port $port2 --get-config ownername |grep Current|sed -e 's/Current:\ //'`

    if [ $camera1 == $1 ]; then
       echo camera1, named $1
       gphoto2 --port $port1 $command $frames $interval
    elif [ $camera2 == $1 ]; then
       echo camera2, named $1
       gphoto2 --port $port2 $command $frames $interval
    fi
