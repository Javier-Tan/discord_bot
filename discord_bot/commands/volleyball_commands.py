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
        page = requests.get(self.FIXTURE_URL)
        soup = BeautifulSoup(page.content, "html.parser")
        # Had to hard code id = image36 for now - may be a better way to find the image

        # If id fails, None.find() error occurs (needs fix)
        result = soup.find(id = "image36").find("a").find("img")
        # find last updated date
        datelist = soup.find(id = "text17").string.split(" ")
        dateobject = datetime.strptime(datelist[-1], '%d/%m/%Y')
        datestring = "As of " + str(dateobject.strftime("%d %b %Y"))
        daysago = " (" + str((datetime.today() - dateobject).days) + " days ago)"
        if result:
            return [datestring + daysago, self.URL + result['data-src']]
        else:
            raise ImageNotFoundException("Fixtures")
    
    async def ranking(self):
        page = requests.get(self.LADDER_URL)
        soup = BeautifulSoup(page.content, "html.parser")
        # Had to hard code id = image32 for now - may be a better way to find the image

        # If id fails, None.find() error occurs (needs fix)
        result = soup.find(id = "image32").find("a").find("img")
        # find last updated date
        datelist = soup.find(id = "text12").string.split(" ")
        dateobject = datetime.strptime(datelist[-1], '%d-%m-%y')
        datestring = "As of " + str(dateobject.strftime("%d %b %Y"))
        daysago = " (" + str((datetime.today() - dateobject).days) + " days ago)"
        if result:
            return [datestring + daysago, self.URL + result['data-src']]
        else:
            raise ImageNotFoundException("Ranking")