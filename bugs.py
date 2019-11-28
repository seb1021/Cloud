#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests

req = requests.get('https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01')

html = req.text

soup = BeautifulSoup(html,'html.parser')

for i in soup.select('.title'):
    print(i.text)

