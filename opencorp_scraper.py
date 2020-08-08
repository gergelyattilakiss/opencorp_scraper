from selenium import webdriver
from bs4 import BeautifulSoup as BS
import csv

class CountryScraper(object):
    def __init__(self,country,page_number):
        self.driver = webdriver.Chrome()
        self.country = country
        self.page_number = page_number
        #use whatever driver engine you have in path (e.g.: Firefox, IE, Safari, Opera)

    def scrape(self):
        self.driver.get("https://opencorporates.com/companies/"+self.country+"?page="+self.page_number+"&q=&utf8=%E2%9C%93")
        #open page with a driver
        soup = BS(self.driver.page_source, 'html.parser')
        writer = csv.DictWriter(open(self.country+self.page_number+'.csv', 'w'), fieldnames = 'name country'.split(' '))
        writer.writeheader()
        for firm in soup.find_all('a', {'class':'company_search_result'}):
            title = firm.get('title').split(' ',7)[7]
            name  = title.split('(', 1)[0][1:-2]
            country = title.split('(',1)[1][0:8]
            dictionary = {'name': name, 'country': country}
            #get the name of the firm and the country it is in
            writer.writerow(dictionary)
        self.driver.close()