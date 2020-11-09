from bs4 import BeautifulSoup

import requests
import re
import json

class WorldSumScraper:
    def __init__(self):
        self.scrape_url = 'https://www.worldometers.info/coronavirus/'
        self.api_sum_world_url = 'http://127.0.0.1:5000/summary/covid/world'
        self.world_summary_data = []
    
    def scrape_data(self):
        soup = self.scrape_page_content()

        if soup:
            self.get_world_sum_data(soup)

            if self.world_summary_data:
                stored_data = self.call_api_put_data(self.world_summary_data)
        
        return stored_data

    def scrape_page_content(self):
        page = requests.get(self.scrape_url)
        soup = BeautifulSoup(page.content, 'html.parser')

        return soup
    
    def get_world_sum_data(self, soup):
        world_sum_data = []

        world_sum_data_html_content = soup.find_all(
            'div', class_='maincounter-number')
        
        for item in range(len(world_sum_data_html_content)):
            regex = r'(\n)|\s'
            data = re.sub(
                regex, '', world_sum_data_html_content[item].text)
            world_sum_data.append(data)
        
        self.world_summary_data = world_sum_data
    
    def call_api_put_data(self, world_summary_data):
        headers = {
            'Content-type': 'application/json',
        }

        data = json.dumps(
            {"sum_world_cases": world_summary_data[0], "sum_world_deaths": world_summary_data[1], "sum_world_recovered": world_summary_data[2]})

        response = requests.put(
            self.api_sum_world_url, headers=headers, data=data)
        
        return response.json()


if __name__ == '__main__':
    wss = WorldSumScraper()
    results = wss.scrape_data()
    print(results)

