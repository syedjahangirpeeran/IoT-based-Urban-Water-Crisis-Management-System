#!/usr/bin/python
import urllib2
import time
import serial
def publish(flowRate, volume, moisture, minwlevel, maxwlevel, turbidity):
	url = "https://karthikeyam.pythonanywhere.com/" +str(flowRate)+"/"+str(volume)+"/"+str(moisture)+"/"+str(minwlevel)+"/"+str(maxwlevel)+"/"+str(turbidity)+"/"+" ".join(str(time.asctime(time.localtime())).split())+"/"
       	print(url)
	result = urllib2.urlopen(url).read()
		
while (True):
	try:
		ser = serial.Serial('/dev/ttyACM0',9600) 
		read_serial=ser.readline()
		L = read_serial.split()
		#print read_serial
		#print L

		flowRate=float(L[0])
		volume=float(L[1])
		moisture=float(L[2])
		minwlevel=float(L[3])
		maxwlevel=float(L[4])
		turbidity=float(L[5])

		print 'Flow Rate= ',flowRate,' L/min' # Temperature in Celcius
		print 'Volume = ',volume,' mL' # The local pressure
		print 'Moisture =', moisture,' %' # The current altitude
		print 'Waterlevel = ',minwlevel,' mm' # The sea-level pressure
		print 'Turbidity Voltage =', (int(turbidity*5.0))/1024.0 # The current altitude
		print str(time.asctime(time.localtime()))
		print 
		publish(flowRate, volume, moisture, minwlevel, maxwlevel, (int(turbidity*5.0))/1024.0)
	
	except: 
		pass
		
	