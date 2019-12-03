#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests

req = requests.get('https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01')


html = req.text

soup = BeautifulSoup(html,'html.parser')

top_list = soup.select('#CHARTrealtime > table > tbody > tr')
top_list2 = soup.select('#CHARTrealtime > table > tbody > tr')
f_song = open("bugs_song.txt","w") #노래 차트 텍스트 파일
f_singer = open("bugs_singer.txt","w") #가수 차트 텍스트 파일

title = [None]*100
singer = [None]*100
n = 0

for i in soup.find_all('p',class_='title'):
    song = i.find('a')
    # print(song.text)
    data_song = "%s\n" % song.text
    f_song.write(data_song) #텍스트파일에 노래 이름 저장
    title[n] = song.text #배열에 노래 이름 저장
    n = n+1

#for i in top_list2:
 #   singer = i.find('td').find('p').find('a')
  #  print(singer.text)
   # data_singer = "%s\n" % singer.text
    #f_singer.write(data.singer)

m = 0
singer2 = [None]*100

for z in soup.find_all('p',class_='artist'):
    singer = z.find('a')
    data_singer = "%s\n" % singer.text
    f_singer.write(data_singer)
    singer2[m] = singer.text #배열에 가수 이름 저장
    m = m+1

for i in range(0,100):
    print("%d위 : %s - %s" %(i+1,title[i],singer2[i]))
