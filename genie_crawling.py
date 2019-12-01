import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.3'}#user info

url = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20191128&hh=18&rtm=Y&pg={}'#page move
#resp = requests.get(url,headers = headers)

#soup = BeautifulSoup(resp.text, 'html.parser')

#songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for n in range(1,4):
    link = url.format(n)
    resp = requests.get(link,headers = headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
    print("page: ",n,"=====================================================")
    for song in songs:
        title = song.find('td',{'class':'info'}).find('a',{'class':'title ellipsis'}).text
        singer = song.find('td',{'class':'info'}).find('a',{'class':'artist ellipsis'}).text
        album = song.find('td',{'class':'info'}).find('a',{'class':'albumtitle ellipsis'}).text

        print(title.strip(),"  ",singer.strip(),"  ",album.strip())#use strip() -> delete blank space
