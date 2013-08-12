timelapse-utilities
===================

code to help deal with time-lapse series

# camera control

I found that my Canon 350Ds were both identifying to my Linux system identically. 
To work around this, I assigned them unique ownernames in the camera settings 
using gphoto2. 

## camera.py

This rewrite supports an unlimited number of cameras and prompts you to select 
a name before taking photographs. see camera.py --help for details.

## camera.sh

The original script. you have to specify the camera name on the command line 
and alter settings in the script directly.
