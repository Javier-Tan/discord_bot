import requests
from bs4 import BeautifulSoup
from discord_bot.exceptions.volleyball_exceptions import ImageNotFoundException

from datetime import datetime

class volleyball_commands(): 
    def __init__(self):
        self.URL = "https://volleyballdays.com/"
        self.FIXTURE_URL = self.URL + "#fixturesun"
        self.LADDER_URL = self.URL + "#laddersun"

    async def fixtures(self):
        ''' Returns a string indicating last updated date, how many days ago that was, and the image URL of the league fixtures'''
        page = requests.get(self.FIXTURE_URL)
        soup = BeautifulSoup(page.content, "html.parser")

        # Had to hard code id = image36 for now - may be a better way to find the image
        # If id fails, None.find() error occurs (needs fix)
        fixtures_image_URL = self.URL + soup.find(id = "image36").find("a").find("img")['data-src']

        # Find last updated date
        last_updated_element_list = soup.find(id = "text17").string.split(" ")
        last_updated_date = datetime.strptime(last_updated_element_list[-1], '%d/%m/%Y')
        last_updated_formatted = last_updated_date.strftime("%d %b %Y")
        # Calculate days ago
        last_updated_days_ago = (datetime.today() - last_updated_date).days
        
        if fixtures_image_URL:
            return f"As of {last_updated_formatted}, ({last_updated_days_ago} days ago) {fixtures_image_URL}"
        else:
            raise ImageNotFoundException("Fixtures")
    
    async def ranking(self):
        ''' Returns a string indicating last updated date, how many days ago that was, and the image URL of the league rankings'''
        page = requests.get(self.LADDER_URL)
        soup = BeautifulSoup(page.content, "html.parser")

        # Had to hard code id = image32 for now - may be a better way to find the image
        # If id fails, None.find() error occurs (needs fix)
        ranking_image_URL = self.URL + soup.find(id = "image32").find("a").find("img")['data-src']

        # Find last updated date
        last_updated_element_list = soup.find(id = "text12").string.split(" ")
        last_updated_date = datetime.strptime(last_updated_element_list[-1], '%d-%m-%y')
        last_updated_formatted = last_updated_date.strftime("%d %b %Y")
        # Calculate days ago
        last_updated_days_ago = (datetime.today() - last_updated_date).days

        if ranking_image_URL:
            return f"As of {last_updated_formatted}, ({last_updated_days_ago} days ago) {ranking_image_URL}"
        else:
            raise ImageNotFoundException("Ranking")