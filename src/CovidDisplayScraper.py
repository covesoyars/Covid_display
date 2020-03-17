"""
Scrapes COVID-19 stats from the web and displays them to the user.

Current data source: https://www.worldometers.info/coronavirus/*


"""
__author__ = 'covesoyars'

from bs4 import BeautifulSoup
import requests
from time import sleep


class CovidDisplay(object):

	"""
	object to scrape current coronavirus stats. Will have a nested dictionary as its main data structure:
	{
		'world_wide':{stats_dict},
		'USA':{stats_dict},
	}


	More can be added afterwards. A dictionary to contain the necessary urls and potentially separate functions for
	each data column will be implemented:

	{
		'world_wide': {'func': self.scrape_worldwide, 'url': 'https://www.worldometers.info/coronavirus/'},
		'USA': {'func': self.scrape_usa, 'url':'https://www.worldometers.info/coronavirus/country/us/'}
	}
	"""
	STATS_DICT1 = {'Coronavirus Cases': 0, 'Deaths': 0, 'Recovered': 0} # the 1 implies that multiple different column
																# configurations can be added by adding more constants

	def __init__(self):

		self.columns_dict = {
								'world_wide': self.STATS_DICT1,
								'USA': self.STATS_DICT1,
							}

		self.colums_aux_dict = {
									'world_wide': {
											'func': self.world_meters_scrape,
											'url': 'https://www.worldometers.info/coronavirus/'},

									'USA': {
											'func': self.world_meters_scrape,
											'url': 'https://www.worldometers.info/coronavirus/country/us/'}
											}

		# functions are stored in these dictionaries so that other sites can be scraped in the future in conjunction
		# with these sites if a new function is written for them.

	def world_meters_scrape(self, column):
		"""
		Scrapes information from worldmeters urls
		:param column:
		:return:
		"""
		request = requests.get(self.colums_aux_dict[column]['url'])
		soup = BeautifulSoup(request.content, 'html.parser')

		for thing in soup.find_all('div', attrs={'id': 'maincounter-wrap'}):
			header, count = thing.text.strip().split(':')
			count = int(count.replace(',', ''))
			self.columns_dict[column][header] = count

	def read(self, interval=5):
		"""
		Listens to stats indefinitey and returns a generator object for constant updates.
		:param interval:
		:return:
		"""
		while True:

			for column in self.colums_aux_dict:
				self.colums_aux_dict[column]['func'](column)

			yield self.columns_dict
			sleep(interval)



