import requests
from bs4 import BeautifulSoup
from exceptions.volleyball_exceptions import ImageNotFoundException

URL = "https://volleyballdays.com/"
FIXTURE_URL = URL + "#fixturesun"
LADDER_URL = URL + "#laddersun"

class volleyball_commands(): 
    async def fixtures():
        page = requests.get(FIXTURE_URL)
        soup = BeautifulSoup(page.content, "html.parser")
        # Had to hard code id = image36 for now - may be a better way to find the image
        result = soup.find(id = "image36").find("a").find("img")
        if result:
            return URL + result['data-src']

    async def ranking():
        page = requests.get(LADDER_URL)
        soup = BeautifulSoup(page.content, "html.parser")
        # Had to hard code id = image32 for now - may be a better way to find the image
        result = soup.find(id = "image32").find("a").find("img")
        if result == None:
            raise ImageNotFoundException
        else:
            return URL + result['data-src']