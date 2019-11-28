import requests
import urllib.parse 
from bs4 import BeautifulSoup
RANK=100
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.3'}
mellon=requests.get("https://www.melon.com/chart/index.htm",headers=headers)
soup=BeautifulSoup(mellon.text,"html.parser")

titles=soup.find_all('div',{'class':'ellipsis rank01'})
songs=soup.find_all('div',{'class':'ellipsis rank02'})

title=[]
song=[]
for t in titles:
    title.append(t.find('a').text)
for s in songs:
    song.append(s.find('span',{'class':'checkEllipsis'}).text)
for i in range(RANK):

    print('title:%s singer:%s'%(title[i].strip(),song[i].strip()))
    

