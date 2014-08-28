#!/usr/bin/env python

from lcd import lcddriver
from i2c import i2c_lib
import urllib
import urllib2
import json
import datetime

#Get current weather conditions
url = 'http://api.openweathermap.org/data/2.5/weather?id=4347778'
response = json.loads(urllib2.urlopen(url).read())

# Parse all needed weather data.
city = response['name']
date = date = datetime.datetime.fromtimestamp(response['dt'])
tempk = int(response['main']['temp'])
tempc = tempk - 273.1
tempf = int(tempc * 1.8 + 32)
humidity = int(response['main']['humidity'])
pressure = float(response['main']['pressure'])/1000
cloud_coverage = int(response['clouds']['all'])

lcd = lcddriver.lcd()
lcd.lcd_clear()

lcd.lcd_display_string(city.upper() + ' WEATHER',1)
lcd.lcd_display_string('T: ' + str(tempk) + 'K, ' + str(tempc) + 'C, ' + str(tempf) + 'F',2)
lcd.lcd_display_string('RH: ' + str(humidity) + '%, BP: ' + str(round(pressure,2)), 3)
lcd.lcd_display_string('CC: ' + str(cloud_coverage) + '%', 4)
