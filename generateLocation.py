import os
import random
import time
import datetime
import sys

deltaTime = datetime.timedelta(seconds=1)

XML_HEADER = '<gpx>'
XML_SAMPLE = '<wpt lat="45.47" lon="9.19"> <time>2006-11-05T16:25:00Z</time> </wpt>'
XML_FOOTER = '</gpx>'

nowTime = datetime.datetime.now()

points = list()

lines=open(sys.argv[1], "r").readlines()

f = open("location.gpx", "w")
f.write(XML_HEADER + "\n")

for l in lines:
	data = l.strip().split("\t")
	obj = dict()
	obj["lat"] = data[0]
	obj["lon"] = data[1]
	points.append(obj)

SAMPLES = 40

curPoints = points
curPoints.append(points[0])

for pId in range(0, len(curPoints)-1):
	x1 = float(curPoints[pId]["lat"])
	y1 = float(curPoints[pId]["lon"])

	x2 = float(curPoints[pId+1]["lat"])
	y2 = float(curPoints[pId+1]["lon"])

	# distance = sqrt(pow(x2-x1) + pow(y2-y1))
	m = (y2 - y1) / (x2 - x1)

	for sample in range(0, SAMPLES):
		deltaX = (x2 - x1) / SAMPLES * sample
		lat = x1 + deltaX
		lon = y1 + m * deltaX
		nowTime = nowTime + datetime.timedelta(seconds=1)
		f.write('<wpt lat="'+str(lat)+'" lon="'+str(lon)+'"> <time>'+str(nowTime.strftime("%Y-%m-%dT%H:%M:%SZ"))+'</time> </wpt>\n')

f.write(XML_FOOTER + "\n")
