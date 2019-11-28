#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests

req = requests.get('https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01')

html = req.text

soup = BeautifulSoup(html,'html.parser')

top_list = soup.select('#CHARTrealtime > table > tbody > tr')

for i in top_list:
    title = i.find('th').find('p').find('a')
    print(title.text)
