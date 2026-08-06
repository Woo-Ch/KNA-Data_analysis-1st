# 실습2. with open으로 파일에 쓰기

# 1단계. with open으로 파일을 쓰기 모드 w, utf-8로 열기
# 2단계. write로 내용을 쓰기(줄을 나눌 땐 줄바꿈 기호)
# 3단계. with 블록이 끝나면 파일이 자동으로 닫힘

with open("bye.txt", "w", encoding="utf-8") as f:
    f.write("수고하셨습니다\n")
    f.write("내일 뵙겠습니다\n")

# 4단계. r 모드로 다시 열어 쓴 내용을 확인
with open("bye.txt", "r", encoding="utf-8") as f:
    read = f.read()

print(read)

# 완료!
