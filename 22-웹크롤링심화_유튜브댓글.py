from selenium import webdriver
import chromedriver_autoinstaller
import time
from selenium.webdriver.common.keys import Keys

cp = chromedriver_autoinstaller.install()
browser = webdriver.Chrome(cp)

browser.get("https://www.youtube.com/watch?v=XW0AadaDDUc")
time.sleep(5)

# 스크롤 살짝 내려주기
browser.find_element_by_css_selector("html").send_keys(Keys.PAGE_DOWN) # 스크롤 끝까지 --> Keys.END
time.sleep(5) # 댓글 생성까지 기다려주기
comments = browser.find_elements_by_css_selector("#content-text")
idx = 0
while True:
    try:
        print(comments[idx].text)
    except:
        print("--------- 크롤링 종료!! ----------")
        break
    idx += 1
    if idx % 20 == 0: # idx가 20의 배수라면?
        browser.find_element_by_css_selector("html").send_keys(Keys.END)
        time.sleep(5)
        comments = browser.find_elements_by_css_selector("#content-text")