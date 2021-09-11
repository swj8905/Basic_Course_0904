from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as par
import os
import datetime

t = datetime.datetime.today().strftime("%Y년 %m월 %d일 %H시 %M분 %S초")

if not os.path.exists("./이미지수집"):
    os.mkdir("./이미지수집")

keyword = input("키워드 입력 >> ")

if not os.path.exists(f"./이미지수집/{keyword} - {t}"):
    os.mkdir(f"./이미지수집/{keyword} - {t}")

encoded = par.quote(keyword) # 한글 --> 특수한 문자열
url = f"https://images.search.yahoo.com/search/images;_ylt=AwrT4R.QADxh75EAM1uJzbkF;_ylu=c2VjA3NlYXJjaARzbGsDYnV0dG9u;_ylc=X1MDOTYwNjI4NTcEX3IDMgRhY3RuA2NsawRjc3JjcHZpZANZUDRUdWpFd0xqSUFMTEJYWF9MLl93Ym9NVEUwTGdBQUFBRFBuTDdCBGZyA3lmcC10BGZyMgNzYS1ncARncHJpZANpTF9idVk5VFM2ZXhldXJNSEFJZndBBG5fc3VnZwMxMARvcmlnaW4DaW1hZ2VzLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMEcXN0cmwDMjcEcXVlcnkDJUVEJThDJThDJUVDJTlEJUI0JUVDJThEJUFDBHRfc3RtcAMxNjMxMzIyMjg2?p={encoded}&fr=yfp-t&fr2=sb-top-images.search&ei=UTF-8&x=wrt"
code = req.urlopen(url)
soup = BeautifulSoup(code, "html.parser")
img = soup.select("a > img")
cnt = 1
for i in img:
    img_url = i.attrs["data-src"]
    req.urlretrieve(img_url, f"./이미지수집/{keyword} - {t}/{cnt}.png") # 이미지 다운로드
    print(f"{keyword} 이미지 수집 완료 {cnt}")
    cnt += 1