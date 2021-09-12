from selenium import webdriver
import time
import chromedriver_autoinstaller

chrome_path = chromedriver_autoinstaller.install()
browser = webdriver.Chrome(chrome_path)
browser.get("https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F")
id = browser.find_element_by_css_selector("#id")
id.send_keys("talingpython")
pw = browser.find_element_by_css_selector("#inputPwd")
pw.send_keys("q1w2e3!@#")
browser.find_element_by_css_selector("#loginBtn").click()
time.sleep(3)
browser.get("http://cafe.daum.net/talingpython")
time.sleep(3)
# 가입인사 게시판 클릭
browser.switch_to.frame("down")
browser.find_element_by_css_selector("#fldlink_lF1R_309").click()
time.sleep(3)
# 글쓰기 버튼 클릭
browser.find_element_by_css_selector("#article-write-btn").click()
time.sleep(3)
# 제목 작성
subject = browser.find_element_by_css_selector("input.title__input")
subject.send_keys("안녕하세요!")
# 본문 작성
browser.switch_to.frame("keditorContainer_ifr")
content = browser.find_element_by_css_selector("#tinymce")
content.send_keys("반갑습니다.")
# 등록 버튼 클릭
browser.switch_to.default_content() # 가장 바깥으로 빠져나옴
browser.switch_to.frame("down")
browser.find_element_by_css_selector("button.btn_g.full_type1").click()
time.sleep(3)
browser.close()