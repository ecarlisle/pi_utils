#!/usr/bin/env python

from subprocess import Popen, PIPE
import subprocess, time, sys, os, re
from lcd import lcddriver
import string

Pin = "12"

Args = ["./dht/DHT", "2302", Pin]

Start = time.time()

lcd = lcddriver.lcd()
lcd.lcd_clear()
lcd.lcd_display_string("Loading...",1)

while True:
	Temp = Humi = Out = ""
	Proc = Popen(Args, stdout=PIPE)
	Out = Proc.stdout.read()
	Proc.stdout.flush()
	
	Temp = re.findall(r'[-]*[0-9]*.[0-9]* C', Out)
	Humi = re.findall(r'[-]*[0-9]*.[0-9]* %', Out)
	
	if len(Temp)>0 and len(Humi)>0:
	
		tempc = float(string.replace(str(Temp[0]),' C',''))
		tempk = int(float(tempc) + 273.1)
		tempf = int(tempc * 1.8 + 32)
		rh = string.replace(Humi[0],' %','%')

		lcd.lcd_clear()
		lcd.lcd_display_string("INDOOR CONDITIONS",1)
		lcd.lcd_display_string('T: ' + str(tempk) + 'K, ' + str(tempc) + 'C, ' + str(tempf) + 'F',2)
		lcd.lcd_display_string("RH: " + rh,3)
		sys.exit()
		break
	else:
		if (time.time() - Start) > 5:
			sys.exit()
	time.sleep(1.3)
