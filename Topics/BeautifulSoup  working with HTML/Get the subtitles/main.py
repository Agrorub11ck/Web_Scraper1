import requests
from bs4 import BeautifulSoup

num = int(input())
url = input()

req = requests.get(url)
if req:
    soup = BeautifulSoup(req.content, 'html.parser')
    text = soup.find_all('h2')
    print(text[num].text)
