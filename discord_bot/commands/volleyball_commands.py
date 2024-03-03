import requests
from bs4 import BeautifulSoup
from discord_bot.exceptions.volleyball_exceptions import ImageNotFoundException, DateNotFoundException
from datetime import datetime

URL = "https://volleyballdays.com/"
FIXTURE_URL = URL + "#fixturesun"
LADDER_URL = URL + "#laddersun"

async def vb_fixtures(imgid: str, dateid: str) -> str:
    ''' Returns a string indicating last updated date, how many days ago that was, and the image URL of the league fixtures '''
    page = requests.get(FIXTURE_URL)
    soup = BeautifulSoup(page.content, "html.parser")

    # Find fixtures image
    try:
        fixtures_image_URL = URL + soup.find(id = imgid).find("a").find("img")['data-src']
    except (AttributeError, KeyError) as e:
        raise ImageNotFoundException("Fixtures")

    # Find last updated date and calculate how many days ago the image was last updated
    try:
        last_updated_element_list = soup.find(id = dateid).find("span").text.split(" ")
    except (AttributeError) as e:
        raise DateNotFoundException("Fixtures")

    last_updated_date = datetime.strptime(last_updated_element_list[-3], '%d/%m/%Y')
    last_updated_formatted = last_updated_date.strftime("%d %b %Y")

    last_updated_days_ago = (datetime.today() - last_updated_date).days

    return f"As of {last_updated_formatted}, ({last_updated_days_ago} days ago) {fixtures_image_URL}"
        
    
async def vb_ranking(imgid: str, dateid: str) -> str:
    ''' Returns a string indicating last updated date, how many days ago that was, and the image URL of the league rankings '''
    page = requests.get(LADDER_URL)
    soup = BeautifulSoup(page.content, "html.parser")

    # Find ranking image
    try:
        ranking_image_URL = URL + soup.find(id = imgid).find("a").find("img")['data-src']
    except (AttributeError, KeyError) as e:
        raise ImageNotFoundException("Ranking")

    # Find last updated date and calculate how many days ago the image was last updated
    try:
        last_updated_element_list = soup.find(id = dateid).string.split(" ")
    except (AttributeError) as e:
        raise DateNotFoundException("Ranking")
    
    last_updated_date = datetime.strptime(last_updated_element_list[-1], '%d-%m-%y')
    last_updated_formatted = last_updated_date.strftime("%d %b %Y")

    last_updated_days_ago = (datetime.today() - last_updated_date).days

    return f"As of {last_updated_formatted}, ({last_updated_days_ago} days ago) {ranking_image_URL}"