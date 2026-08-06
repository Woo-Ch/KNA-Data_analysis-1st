# 실습3. a모드로 기록 이어붙이기

# 1단계. with open으로 파일을 추가 모드 a로 열기
# 2단계. write로 새 기록 문장을 쓰기
# 3단계. w 모드와 달리 기존 내용이 보존됨을 확인

with open("bye.txt", "a", encoding="utf-8") as f:
    f.write("조심히 들어가세요")

# 4단계 r 모드로 열어 전체가 쌓였는지 확인
with open("bye.txt", "r", encoding="utf-8") as f:
    read = f.read()

print(read)

# 완료!!
