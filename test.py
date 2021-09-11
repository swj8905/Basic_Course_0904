from selenium import webdriver
import chromedriver_autoinstaller
import time

cp = chromedriver_autoinstaller.install()
browser = webdriver.Chrome(cp)
browser.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")

# 로그인 하기
id = browser.find_element_by_css_selector("input#id")
id.send_keys("talingpython")
pw = browser.find_element_by_css_selector("input#pw")
pw.send_keys("q1w2e3!@#")
button = browser.find_element_by_css_selector("button.btn_login")
button.click()