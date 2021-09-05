from bs4 import BeautifulSoup
import urllib.request as req


# 서버한테 요청메시지 보내고, HTML 코드 받기
code = req.urlopen("http://www.cgv.co.kr/movies/")
# print(code.read())

# HTML 코드 이쁘게 정리하기
soup = BeautifulSoup(code, "html.parser")
# print(soup)

# 내가 원하는 요소 알려주기
title = soup.select_one("strong.title")
print(title.string)