from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient
client = MongoClient('mongodb://test:test@localhost', 27017)
# client = MongoClient('localhost', 27017)
db = client.dbeverybody_salad

# 코딩 시작



#naver salad crawling part start


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

for i in range(3):
    j = f'https://terms.naver.com/list.naver?cid=48166&categoryId=48166&page={i+1}';
    data = requests.get(j, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    trs = soup.select('#content > div.list_wrap > ul > li')
    for tr in trs:
        name = tr.select_one('div.info_area > div.subject > strong > a').text.split('만드는 법')[0]
        desc = tr.select_one('div.info_area > p').text.lstrip()
        thumb = tr.select_one('div.thumb_area > div.thumb > a > img')['data-src']
        url = tr.select_one('div.info_area > div.subject > strong > a')['href']

        doc = {
            'salad name': name,
            'salad desc': desc,
            'salad thumb': thumb,
            'salad url':'https://terms.naver.com'+url
        }
        db.salad.insert_one(doc)



#naver salad crawling part end