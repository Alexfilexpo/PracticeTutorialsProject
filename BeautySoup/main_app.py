import urllib3
import re
from bs4 import BeautifulSoup

year = "2018"

base_url = "https://www.metacritic.com"
url = "https://www.metacritic.com/browse/games/score/metascore/year/pc/filtered?year_selected=" + year + "&sort=desc"
ourUrl = urllib3.PoolManager().request('GET', url).data
soup = BeautifulSoup(ourUrl, "lxml")

i = 1
gamesList = soup.find_all("li", class_=re.compile(r'product game_product'))

for item in gamesList:
    title = item.findChild('a').text.strip()
    game_url = base_url + item.findChild('a')['href']
    print(game_url)
    print(title)