# 파일 열기 모드
# w 모드 : 쓰기모드
#   - 파일이 존재하지 않으면, 자동으로 생성해줌
#   - 파일의 내용을 모두 지운 후, 연다.
# a 모드 : 더해서 쓰기모드
#   - 파일이 존재하지 않으면, 자동으로 생성해줌
#   - 파일의 내용을 모두 유지한 후, 연다.
f = open("./test.txt", "w")
f.write("Hello World\n")
f.write("Hello Python")
f.close()