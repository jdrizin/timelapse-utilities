#!/usr/bin/env python2.7

from subprocess import check_output, call
import argparse
from re import findall

#define parsers.
parser = argparse.ArgumentParser(description="""Control two Canon dSLR cameras 
	of the same model using the ownername camera feature. Requires the gphoto2 
	binary in your $PATH. Images download in the current working directory""", 
	epilog="""This will prompt you for the camera name from those detected. 
	Capture begins after you hit Enter. Your camera may not be able to sustain 
	5s between shots, so play around with the interval setting""") 
parser.add_argument('-f', action='store', dest='frames', default='1440', 
	help="""number of frames to capture. default is 1440""")
parser.add_argument('-i', action='store', dest='interval', default='5', 
	help="""interval to wait between frames in seconds. default is 5s""")
parser.add_argument('-c', action='store_const', dest='command', 
	default='--capture-image-and-download', const='--capture-image', 
	help="""keep the images on the card. only enable this if you have a large 
	enough memory card in your camera""")
args = parser.parse_args()

# returns a list of usb port IDs for use with gphoto2
def findCameraID( lines ):
	return(findall(r"(usb:...,...)", lines))

# use this on elements from a list to return a (port,name) object
def getCameraName( port ):
	ownerText = check_output(['gphoto2', '--port', port, '--get-config', 'ownername'])
	cameraName = findall(r"Current: (.+)\n", ownerText)[0]
	return([port, cameraName])

cameras = check_output(['gphoto2', '--auto-detect']) #get the output from gphoto2
ids = findCameraID(cameras) #strip the usb:ids from raw gphoto2 output
names = [getCameraName(id) for id in ids] #output a list of names

if len(names) == 0:
	exit("No cameras detected. Are they turned on and plugged in?")

print 'detected cameras: ', [name[1] for name in names] #list the cameras

cameraName = raw_input('Please type in the camera name: ') #prompt for camera name

portName = [name[0] for name in names if name[1] == cameraName][0] #extract usb port name

call(['gphoto2', '--port', portName, args.command, '-F', args.frames, '-I', args.interval])