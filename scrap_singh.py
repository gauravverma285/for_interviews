import requests
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/user/PewDiePie'
page = requests.get(url)
print(page, 'AAAAAAAAAAAAAAAAA')

soup = BeautifulSoup(page.text, "html.parser")
# print(soup, 'CCCCCc')

pew = soup.findAll("span", {"class": "masthead_custom_styles"})

print(pew, "BBBBBBBBBBBBBBB")