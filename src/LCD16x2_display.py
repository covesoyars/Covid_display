from CovidDisplayScraper import CovidDisplay

import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd
from time import sleep

"""Displays COVID-19 stats on LCD 16x2 screen"""

# initialize LCD:
lcd_columns = 16
lcd_rows = 2

lcd_rs = digitalio.DigitalInOut(board.D22)
lcd_en = digitalio.DigitalInOut(board.D17)
lcd_d4 = digitalio.DigitalInOut(board.D25)
lcd_d5 = digitalio.DigitalInOut(board.D24)
lcd_d6 = digitalio.DigitalInOut(board.D23)
lcd_d7 = digitalio.DigitalInOut(board.D18)

lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
									  lcd_d7, lcd_columns, lcd_rows)



for data in CovidDisplay().read():

	for column in data:		# for each country, for now:

		for header in data[column]:

			lcd.message = column + " " + header
			sleep(5)
			lcd.clear()






