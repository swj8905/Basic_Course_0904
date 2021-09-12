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
# 중고나라 게시판 클릭
browser.switch_to.frame("down")
browser.find_element_by_css_selector("#fldlink_rRa6_347").click()
time.sleep(3)

# 메모장에 있는 제목들 읽어들임
try:
    f = open("./중고나라.txt", "r")
    ref = f.readlines() # ref : 리스트형
    f.close()
except:
    f = open("./중고나라.txt", "w")
    ref = []
    f.close()

# 게시판 제목 크롤링
title = browser.find_elements_by_css_selector("a.txt_item")
new_one = 0
for i in title:
    if (i.text+"\n") not in ref: # 최신 글이라면?
        f = open("./중고나라.txt", "a") # a 모드 : 더해서 쓰기모드
        f.write(i.text + "\n")
        f.close()
        if "에어컨" in i.text:
            new_one += 1
print(f"에어컨 관련 글이 {new_one}개 올라왔습니다.")
browser.close()

if new_one >= 1:
    from twilio.rest import Client

    account_sid = "ACefe43744d5ca8b39d239f2a622c277e0"
    auth_token = "98b8d3f394db1508d72eadf8ae9be131"
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=f"에어컨 관련 글이 {new_one}개 올라왔습니다. https://cafe.daum.net/talingpython/rRa6",
                         from_='+14703090526',
                         to='+821095518905'
                     )