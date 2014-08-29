#!/usr/bin/env python
 
from time import sleep
import os
import RPi.GPIO as GPIO

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.IN)
GPIO.setup(10, GPIO.IN)
GPIO.setup(11, GPIO.IN)
 
while True:
        if ( GPIO.input(10) == False ):
                os.system("./movie_quote.py")
        if ( GPIO.input(11) == False ):
                os.system("./weather.py")
        if ( GPIO.input(9) == False ):
                os.system("./temp_hum.py")
	sleep(0.1)
