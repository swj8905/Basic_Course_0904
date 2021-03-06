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

#메모장 제목들 읽어들임
try:
    f = open("./중고나라.txt", "r")
    ref = f.readlines()
    f.close()

except:
    f = open("./중고나라.txt", "w")
    ref = []
    f.close()

#게시판 제목 크롤링
title = browser.find_elements_by_css_selector("a.txt_item")
new_one = 0
for i in title:
    if (i.text + "\n") not in ref: #최근에 올라온 글이라면
        f = open("./중고나라.txt", "a") #a모드: 더해서 쓰기 모드
        f.write(i.text + "\n")
        if "에어컨" in i.text:
            new_one += 1

print(f"에어컨 관련 글이 {new_one}개 올라왔습니다.")
browser.close()

if new_one >= 1:
    from twilio.rest import Client


account_sid = "ACc3a26b7092bed6edb437b19fe0d20b99"
auth_token = "dc1ed4d0cea890e1b3cb28c31704ab00"
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body=f"에어컨 관련 글이 {new_one}개 올라왔습니다. https://cafe.daum.net/talingpython/rRa6",
                     from_='+12025248670',
                     to='+821099097378'
                 )