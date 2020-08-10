from selenium import webdriver
from bs4 import BeautifulSoup as BS
import csv
import re
from unidecode import unidecode

sk = re.compile(r'[0-9]+, ([A-Za-z\s\/\(\)\.]+)[,\s0-9\<]*')


class CountryScraper(object):
    def __init__(self,country,page_number):
        self.driver = webdriver.Chrome()
        self.country = country
        self.page_number = page_number
        #use whatever driver engine you have in path (e.g.: Firefox, IE, Safari, Opera)

    def scrape(self):
        self.driver.get("https://opencorporates.com/companies/"+self.country+"?commit=Go&inactive=false&order=&page="+self.page_number+"&q=&utf8=%E2%9C%93")
        #open page with a driver
        soup = unidecode(BS(self.driver.page_source, 'html.parser'))
        writer = csv.DictWriter(open(self.country+self.page_number+'.csv', 'w'), fieldnames = 'name country city'.split(' '))
        if self.country not in ['sk', 'ro']:
            for firm in soup.find_all('li', {'class':'search-result company '}):
                title_res = firm.find('a', {'class' : 'company_search_result'})
                add_res = firm.find('span', {'class': 'address'})
                add = str(firm)
                title = title_res.get('title').split(' ', 7)[7].strip('"')
                name = title.split('(', 1)[0][1:-1]
                country = title.split('(',1)[1].split(',')[0]
                if country == "Croatia":
                    city = add.split(',')[-2]
                if country == "Slovenia":
                    city = add.split(' ')[-1].split('<')[0]
                if country == "Poland":
                    city = " "
                dictionary = {'name': name, 'country': country, 'city': city}
                writer.writerow(dictionary)

        if self.country == "sk":
            for firm in soup.find_all('li', {'class':'search-result company '}):
                title_res = firm.find('a', {'class' : 'company_search_result'})
                add_res = firm.find('span', {'class': 'address'})
                add = str(firm)
                title = title_res.get('title').split(' ', 7)[7]
                name = title.split('(', 1)[0][1:-1].strip('"')
                country = title.split('(',1)[1].split(',')[0]
                try:
                    city = sk.search(add).groups()
                except AttributeError:
                    city = ""
                dictionary = {'name': name, 'country': country, 'city': city}
                writer.writerow(dictionary)

            for firm in soup.find_all('li',{'class':'search-result company v_lividácii'}):
                title_res = firm.find('a', {'class' : 'company_search_result'})
                add_res = firm.find('span', {'class': 'address'})
                add = str(firm)
                title = title_res.get('title').split(' ', 7)[7]
                name = title.split('(', 1)[0][1:-1].strip('"')
                country = title.split('(',1)[1].split(',')[0]
                try:
                    city = sk.search(add).groups()
                except AttributeError:
                    city = ""
                dictionary = {'name': name, 'country': country, 'city': city}
                writer.writerow(dictionary)

        if self.country == "ro":
            for firm in soup.find_all('li', {'class':'search-result company '}):
                title_res = firm.find('a', {'class' : 'company_search_result'})
                add_res = firm.find('span', {'class': 'address'})
                add = str(firm)
                title = title_res.get('title').split(' ', 7)[7]
                name = title.split('(', 1)[0][1:-1].strip('"')
                country = title.split('(',1)[1].split(',')[0]
                city = add.split(',')[-1].split('<')[0]
                dictionary = {'name': name, 'country': country, 'city': city}
                writer.writerow(dictionary)

            for firm in soup.find_all('li',{'class':'search-result company functiune'}):
                title_res = firm.find('a', {'class' : 'company_search_result'})
                add_res = firm.find('span', {'class': 'address'})
                add = str(firm)
                title = title_res.get('title').split(' ', 7)[7]
                name = title.split('(', 1)[0][1:-1].strip('"')
                country = title.split('(',1)[1].split(',')[0]
                city = add.split(',')[-1].split('<')[0]
                dictionary = {'name': name, 'country': country, 'city': city}
                writer.writerow(dictionary)

            for firm in soup.find_all('li',{'class':'search-result company intrerupere_temporara_de_activitate'}):
                title_res = firm.find('a', {'class' : 'company_search_result'})
                add_res = firm.find('span', {'class': 'address'})
                add = str(firm)
                title = title_res.get('title').split(' ', 7)[7]
                name = title.split('(', 1)[0][1:-1].strip('"')
                country = title.split('(',1)[1].split(',')[0]
                city = add.split(',')[-1].split('<')[0]
                dictionary = {'name': name, 'country': country, 'city': city}
                writer.writerow(dictionary)

        self.driver.close()