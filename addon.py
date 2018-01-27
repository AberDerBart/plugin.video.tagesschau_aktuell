import sys
import xbmc

def getCurrentVideoUrl():
	return 'http://media.tagesschau.de/video/2018/0127/TV-20180127-1308-3901.webml.h264.mp4'

xbmc.Player().play(getCurrentVideoUrl())
