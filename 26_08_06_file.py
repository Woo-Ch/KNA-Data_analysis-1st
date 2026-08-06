# 기본 내장함수인 open()으로 sample.txt 파일 열기
# 읽기모드 (r)로 utf-8 형식의 반환을 거쳐 읽기로 한다
# 가져온 정보(파일 접근 열쇠/참조값)를 f에 담는다

f = open("sample.txt", "r", encoding="utf-8")

print(type(f).__name__)  # 타입의 이름 TextIOWrapper

# 텍스트파일 파일 한줄씩 문자열 만들기
lines = f.readlines()
print(lines)
# 프린트시 출력되는 \n은 줄바꿈 표시

f.close()  # 열었다면 언젠가는 꼭 닫아줍시다

# ==== 주의사항 1 ====
# open을 하고 나서, read를 하면 커서는 이미 끝까지 갔기 때문에
# 한번 더 read나 readlines 등을 하더라도
# 빈 리스트를 출력한다.
# 그렇기 때문에 한번 더 read를 하거나 다른 파일을 read를 하려면
# 다시 open을 작성해서 코드를 짜야 함.

# ==== 주의사항 2 ====
# 폴더를 다르게 해서 sample.txt를 만들고 실행해도
# 처음 만든 sample.txt를 출력하는 이유는
# python debugger는 폴더를 다르게 하더라도 전체 경로를 사용하기 때문에
# 의미가 없다. 그렇기 때문에 os.path.join을 사용해서 경로를 확실하게 지정하자.

# 만약 신경써서 파일 닫기 (close) 해주기 귀찮다면
# with open ... as 문법을 쓰는 것도 좋다
with open("sample.txt", "r", encoding="utf-8") as f:
    # 앞으로 이렇게 들여쓰기 된 코드가 끝나면
    # 파일 접근을 닫습니다(close)

    # 텍스트파일 파일 한줄씩 문자열을 만들어 리스트만들기
    lines = f.readlines()

print(lines)  # print는 들여쓰기에서 빼도 됨
# 들여쓰기된 코드 끝나면 끝난걸로 보기 때문에 close를 사용하지 않아도 된다.

print("============== 3교시 ===============")

# 쓰기모드(write)로 파일을 새롭게 만들어보겠습니다
f = open("hello.txt", "w", encoding="utf-8")

# 파일 쓰기에 줄바꿈을 포함하려면 \n을 포함시킨다
f.write("안녕하세요\n")
# 파일 쓰기에 들여쓰기를 포함하려면
f.write("\t반갑습니다\n")
# 탭 들여쓰기라고 부릅니다.
# 끝에 \n으로 줄바꿈은 국룰느낌

f.close()

# 이어쓰기 모드(append)로 파일에 내용을 추가합시다

f = open("hello.txt", "a", encoding="utf-8")

f.write("맛점하세요\n")

f.close()

