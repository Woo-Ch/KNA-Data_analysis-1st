# 실습1. open으로 파일 읽기

# 1단계. open으로 파일을 읽기 모드 r, utf-8로 열기

f = open("sample.txt", "r", encoding="utf-8")

# 2단계. read로 전체를 한 문자열로 읽어 출력
read_f = f.read()

print(read_f)

f.close()

# 3단계. readlines로 줄 리스트로 읽어 출력
f = open("sample.txt", "r", encoding="utf-8")

readlines_f = f.readlines()

print(readlines_f)

f.close()

# 4단계. 두 방식의 결과 차이를 비교하고 파일을 close

# 2단계는 줄바꿈 표시 없음. 그냥 내용 출력
# 3단계는 ['Hello World\n', 'Bye World'] 형식과 같이 \n으로 줄바꿈 표시함.
