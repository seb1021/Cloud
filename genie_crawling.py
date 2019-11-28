import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.3'}

url = 'https://www.genie.co.kr/chart/top200'
resp = requests.get(url,headers = headers)
soup = BeautifulSoup(resp.text, 'html.parser')

song = soup.find("a",{"class": "title ellipsis"}).text

print(song)
