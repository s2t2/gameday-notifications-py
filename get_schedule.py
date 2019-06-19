from pprint import pprint
import os
import textwrap
import requests
from bs4 import BeautifulSoup

#SCHEDULE_PAGES = {
#    "2018-2019": "https://www.uconnhuskygames.com/2018/07/wbb-2018-2019-game-replays.html",
#    "2018-2019": "https://www.uconnhuskygames.com/2018/07/wbb-2017-2018-game-replays.html",
#    "2018-2019": "https://www.uconnhuskygames.com/2018/07/wbb-2016-2017-game-replays.html"
#}
#request_url = SCHEDULE_PAGES["2018-2019"]
#response = requests.get(request_url)
#print(type(response))
#print(response.status_code)
#soup = BeautifulSoup(response.text, features="html.parser")
#print(type(soup))

html_filepath = os.path.join(os.path.dirname("__file__"), "huskygames", "schedule_page_2019.html")
with open(html_filepath) as html_file:
    content = html_file.read()
soup = BeautifulSoup(content, features="html.parser")
print(type(soup))

print("TABLES:")
tables = soup.findAll("table")
print(len(tables))
for table in tables:
    print(type(table)) #> <class 'bs4.element.Tag'>
    pprint(table.attrs) #> {'align': 'center', 'style': 'width:100%'}
    print(textwrap.shorten(table.text, width=60, placeholder="..."))
    print("-------------------------------")

# geno_show_table = soup.find("table", "___") # hmmm how to identify these tables...

#geno_show_table = [t for t in tables if "The Geno Auriemma Show" in t.text]
#
#print("GENO SHOW")
