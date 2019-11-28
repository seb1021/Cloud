import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.3'}#user info

url = 'https://www.genie.co.kr/chart/top200'
resp = requests.get(url,headers = headers)

soup = BeautifulSoup(resp.text, 'html.parser')


songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for song in songs:
    title = song.find('td',{'class':'info'}).find('a',{'class':'title ellipsis'}).text
    print(title.strip())#use strip() -> delete blank space

