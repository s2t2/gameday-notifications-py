
import requests
from bs4 import BeautifulSoup

SCHEDULE_PAGES = {
    "2018-2019": "https://www.uconnhuskygames.com/2018/07/wbb-2018-2019-game-replays.html",
    "2018-2019": "https://www.uconnhuskygames.com/2018/07/wbb-2017-2018-game-replays.html",
    "2018-2019": "https://www.uconnhuskygames.com/2018/07/wbb-2016-2017-game-replays.html"
}

request_url = SCHEDULE_PAGES["2018-2019"]

response = requests.get(request_url)
print(type(response))
print(response.status_code)

soup = BeautifulSoup(response.text, features="html.parser")
print(type(soup))

# geno_show_table = soup.find("table", "___") # hmmm how to identify these tables...
