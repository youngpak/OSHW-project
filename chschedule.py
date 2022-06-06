from urllib import response
import requests
from bs4 import BeautifulSoup
import re

url="https://www3.chosun.ac.kr/chosun/index...do?main=Y"

response = requests.get(url)

if response.status_code ==200:
    html = response.text
    soup = BeautifulSoup(html,'html.parser')
    schedule= soup.select('div.scheduleMain li > p')
    
else:
    print(response.status_code)

f = open('sche.txt','w',encoding='utf-8')

for element in schedule:
    TEXT = re.sub("\t|\n", "", element.text)
    f.write(TEXT)
    f.write('\n')

f.close()