import requests
from bs4 import BeautifulSoup
from exceptions.volleyball_exceptions import ImageNotFoundException

class volleyball_commands(): 
    def __init__(self):
        self.URL = "https://volleyballdays.com/"
        self.FIXTURE_URL = self.URL + "#fixturesun"
        self.LADDER_URL = self.URL + "#laddersun"

    async def fixtures(self):
        page = requests.get(self.FIXTURE_URL)
        soup = BeautifulSoup(page.content, "html.parser")
        # Had to hard code id = image36 for now - may be a better way to find the image
        result = soup.find(id = "image36").find("a").find("img")
        if result:
            return self.URL + result['data-src']
        else:
            raise ImageNotFoundException("Fixtures")

    async def ranking(self):
        page = requests.get(self.LADDER_URL)
        soup = BeautifulSoup(page.content, "html.parser")
        # Had to hard code id = image32 for now - may be a better way to find the image
        result = soup.find(id = "image32").find("a").find("img")
        if result:
            return self.URL + result['data-src']
        else:
            raise ImageNotFoundException("Ranking")