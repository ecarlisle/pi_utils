#!/usr/bin/env python

# loading the class
import lcddriver
import random
import time
import sys

# lcd start
lcd = lcddriver.lcd()

# this command clears the display (captain obvious)
lcd.lcd_clear()

#open quotes file.
file = open("/home/pi/projects/pi_lcd/quotes.txt","r")
lines = file.readlines()

def loadLCD(content):

	lcd_rows = 4
	current_row = 1
	max_row_length = 19
	line_text = ''
	word_arr = content.split()

	for word in word_arr:
		if len(word) + len(line_text) < 20:
			if line_text != '': 
				line_text += ' '
			line_text += word
		else:
			lcd.lcd_display_string(line_text, current_row)
			current_row += 1
			line_text = word
	if current_row > lcd_rows:
		sys.exit()
	if line_text != '':
		lcd.lcd_display_string(line_text, current_row)

quote = random.choice(lines).strip()
loadLCD(quote);
