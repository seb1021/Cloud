#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests

req = requests.get('https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01')


html = req.text

soup = BeautifulSoup(html,'html.parser')

top_list = soup.select('#CHARTrealtime > table > tbody > tr')
top_list2 = soup.select('#CHARTrealtime > table > tbody > tr > td > p > a')
f_song = open("bugs_song.txt","w") #노래 차트 텍스트 파일
f_singer = open("bugs_singer.txt","w") #가수 차트 텍스트 파일

for i in top_list:
    song = i.find('th').find('p').find('a')
    print(song.text)
    data_song = "%s\n" % song.text
    f_song.write(data_song)

#for i in top_list2:
 #   singer = i.find('td').find('p').find('a')
  #  print(singer.text)
   # data_singer = "%s\n" % singer.text
    #f_singer.write(data.singer)

for i in soup.find_all('p',class_='artist'):
    singer = i.find('a')
    print(singer.text)
    data_singer = "%s\n" % singer.text
    f_singer.write(data_singer)


