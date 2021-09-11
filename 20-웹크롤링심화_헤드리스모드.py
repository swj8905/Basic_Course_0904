from selenium import webdriver
import chromedriver_autoinstaller
import time

cp = chromedriver_autoinstaller.install()

opt = webdriver.ChromeOptions()
opt.add_argument("headless")

browser = webdriver.Chrome(cp, options=opt)
browser.get("https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F")

# 로그인 하기
id = browser.find_element_by_css_selector("input#id")
id.send_keys("talingpython")
pw = browser.find_element_by_css_selector("input#inputPwd")
pw.send_keys("q1w2e3!@#")
button = browser.find_element_by_css_selector("button#loginBtn")
button.click()
time.sleep(3) # 로그인이 다 될때까지 기다리기

# 이메일함으로 이동
browser.get("https://mail.daum.net/")
time.sleep(2) # 웹페이지 다 뜰때까지 기다리기

# 이메일 제목을 크롤링
title = browser.find_elements_by_css_selector("strong.tit_subject")
for i in title:
    print(i.text) # bs4 : .string / selenium : .text
browser.close()