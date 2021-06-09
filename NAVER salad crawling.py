from bs4 import BeautifulSoup
import requests



#naver salad crawling part start


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://terms.naver.com/list.naver?cid=48166&categoryId=48166',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

#content > div.list_wrap > ul > li:nth-child(1)
#content > div.list_wrap > ul > li:nth-child(2)

trs = soup.select('#content > div.list_wrap > ul > li')
for tr in trs :
    name = tr.select_one('div.info_area > div.subject > strong > a').text
    desc = tr.select_one('div.info_area > p').text
    print(name)


# title = soup.select_one('#content > div.list_wrap > ul > li:nth-child(1) > div.info_area > div.subject > strong > a:nth-child(1)')
#content > div.list_wrap > ul > li:nth-child(2) > div.info_area > div.subject > strong > a:nth-child(1)
#content > div.list_wrap > ul > li:nth-child(1) > div.thumb_area > div.thumb.id1988477 > a:nth-child(1) > img
#content > div.list_wrap > ul > li:nth-child(1) > div.info_area > p
#
# print(title.text)

#naver salad crawling part end