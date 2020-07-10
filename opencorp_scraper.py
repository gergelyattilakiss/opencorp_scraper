from selenium import webdriver
from bs4 import BS
import csv

link = "https://opencorporates.com/companies/sk?q=&utf8=%E2%9C%93"

class CountryScraper(object):
	def __init__(self):
		self.driver = webdriver.Chrome()
		#use whatever driver engine you have in path (e.g.: Firefox, IE, Safari, Opera)

	def scrape_country(self):
		self.driver.get(link)
		soup = BS(self.driver.page_source, 'html.parser')
		writer = csv.DictWriter(open('where_sample.csv', 'w'), fieldnames = 'name country'.split(' '))
			for firm in soup.find_all('a', {'class':'company_search_result'}):
				title = firm.get('title').split(' ',7)[7]
				name  = title.split('(', 1)[0][1:-2]
    			country = title.split('(',1)[1][0:8]
    			dictionary = {'name': name, 'country': country}
    			wirter.writerow(dictionary)
		self.driver.close()

	def scrape(self):
		self.scrape_country()

		#scrapethissite.com