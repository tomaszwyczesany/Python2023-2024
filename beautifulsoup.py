import requests
from bs4 import BeautifulSoup
res = requests.get("http://scanme.nmap.org")
page = BeautifulSoup(res.text, "html.parser")


print(page.find_all('a')