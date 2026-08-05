# """ """ - 여러 줄 문자열

notice = """설비 점검 안내
1. 전원 확인
2. 센서 점검"""

print(notice)

#
# 설비 점검 안내
# 1. 전원 확인
# 2. 센서 점검
# 
# 위와 같이 직접 작성한 줄바꿈이 반영되어 여러 줄로 출력함

# 작성하는 개발자가 보기 편한 방식으로 출력했을 때 문제
notice = """
설비 점검 안내
1. 전원 확인
2. 센서 점검
"""
# 개발자가 보기 편한 방식으로 작성하면 생각과 다른 결과물이 나옴
# """ """ (삼중 따옴표를 사용할 시 그 내부의 모든 줄바꿈이 다 반영되어 출력)
# 삼중 따옴표는 탭도 그대로 유지

# =======================
# 이스케이프 문자
print("=== 이스케이프 문자 ===")

# \n - 줄바꿈
notice = "설비 점검 안내\n1. 전원 확인\n2. 센서 점검"
print(notice)

# \t 탭
tap = "이름\t상태"
print(tap) # 이름   상태

backslash = "이름\\상태"
print(backslash) # 이름\상태
# 첫번째 \는 이스케이프 문자라는 것을 알리는 용도

quotes = 'It\'s me' 
print(quotes)
# 감싸는 따옴표와 str 내부 따옴표의 종류가 같을 때는 \를 사용

# 빈 문자열과 공백 문자열의 차이
# "" 따옴표로 감싸졌지만 아무것도 작성되지 않았다면 빈 문자열
# 빈 문자열은 글자 수 0, 길이 0
# " " 따옴표 안에 공백(스페이스바)이 있는 경우는 "공백 문자열"
# 공백(스페이스바)의 수 만큼 글자가 있고, 길이가 세어짐
# 빈 문자열과 공백 문자열은 컴퓨터에게 다른 값으로 인식됨
print("" == " ") # False

# 실습. 설비 정보 출력 카드 만들기
code = "PUMP_A"
state = "정상"
hour = 1200
date = "2026-07-16"

card = "설비: " + code + "\n상태: " + state + "\n가동: " + str(hour) + "\n점검: " + date
print(card)
# 변수에 저장할 때에는 쉼표보단 더하기를 사용하자
# 쉼표를 쓰면 변수는 쉼표 사이사이마다 별개의 것으로 인식하기 때문

# ==========================================
print("=== 인덱싱 ===")
# 인덱싱 - 위치 번호로 글자를 하나 꺼내기
# 문자열[인덱스번호]
# 문자열의 첫 글자 인덱스는 0

word = "PYTHON"
print(word[0], word[3], word[5]) # P H N

abc = "abcdefghijklmnopqrstuvwxyz"
print(abc[12] + abc[8] + abc[13] + abc[22] + abc[14] + abc[14]) # minwoo

# 음수 인덱스는 뒤에서부터 역순으로 순서 숫자가 붙음
# 주의사항은 음수 인덱스는 가장 마지막 글자가 -1부터 시작

# 인덱스 범위를 벗어나면 IndexError 오류가 발생
# 이유는 변수에 저장된 문자열의 길이보다 큰 인덱스를 호출했기 때문에

# ==========================================
print("=== 슬라이싱 ===")

# 슬라이싱 - 구간으로 잘라내기
# 문자열[시작:끝]
# 시작 인덱스 글자는 포함해서 출력
# 끝 인덱스 글자는 제외하고 출력

word = "PYTHON"
print(word[3:5]) # HO
print(word[3:6]) # HON
# print(word[6]) # Error -> 인덱싱은 정확하게 마지막 인덱스까지만 쓸 수 있고, 넘치면 Error
# 슬라이싱은 end가 포함되지 않고 출력하기 때문에 없는 인덱스인 6도 사용할 수 있음

# 슬라이싱 start 생략
# 처음부터 특정 인덱스까지 구간을 뽑아내고 싶을 때 사용
print(word[:4]) # print(word[0:4])와 동일한 동작

# 슬라이싱 end 생략
# 특정 인덱스부터 끝까지 구간을 뽑아내고 싶을 때 사용
print(word[2:]) # 2번 인덱스부터 끝까지 출력
# print(word[2:6])과 동일한 동작

# 슬라이싱 전체 생략
print(word[:]) # print(word[0:6])과 동일한 동작
# :을 사용하고 start와 end를 모두 생략하면 모든 인덱스의 구간을 뽑아냄

# 슬라이싱 음수 인덱스 사용
print(word[-3:]) # HON
# 음수 인덱스 작성 시 그냥 그 인덱스부터 정방향으로 출력함
print(word[:-1]) # PYTHO
# 처음부터 -1(5)를 제외한 구간을 뽑아냄
# 역순 아님 주의
# 음수 인덱스 사용 시 컴퓨터가 알아서 정수 인덱스 찾아 치환해서 동작

# step으로 건너뛰기
# 문자열[시작:끝:간격]
print(word[0:6:2]) # PTO
# PYTHON에서 첫 번째 글자는 명시했으니 거기서부터 출력
# step이 2이기 때문에 Y는 건너뛰고, T
# H는 건너뛰고, O
# N은 건너뛰고, 그 뒤로는 없으므로, PTO가 출력됨
# 두 글자를 뛰는게 아니라 두 번 뛰는 것

# start와 end를 생략하고 step만 입력할 경우
print(word[::2]) # word 변수의 모든 글자를 두 칸씩 뛰면서 출력해줌 # PTO 출력

# 순서 뒤집기
print(word[::-1]) # NOHTYP
# step은 인덱스가 아니고, 음수 입력 시 문자열의 순서를 뒤집음

# 슬라이싱은 범위를 벗어나도 오류가 발생하지 않음
print("범위를 벗어난 슬라이싱", word[0:100:1]) # PYTHON 정상 출력

# =========================================
# len() - 문자열의 길이 반환
# len(문자열)

print(len("hello World!")) # 12 (공백도 모두 글자 취급)
print(len("")) # 0 (빈 문자열은 0 출력)

var = "여러분~! 한 시간만 더 하면 됩니다! 조금만 더 힘을 내주세요!"
print(len(var)) # 36 (변수에 담긴 문자열의 길이 출력도 가능)

print(len("이것도") - len("가능할까?")) # -2
# len()은 int를 반환하기 때문에 연산 가능

abc = "abcdefghijklmnopqrstuvwxyz"
print("abc 변수의 길이:", len(abc), " / 마지막 인덱스 번호:", len(abc) - 1)
# abc 변수의 길이: 26  / 마지막 인덱스 번호: 25

# 음수 인덱스를 사용하지 않고 마지막 인덱스 문자를 뽑고 싶을 때
print(abc[len(abc) - 1])

# in - 특정 문자가 문자열에 포함되어있는지 여부 확인
# "여부"를 확인하기 때문에 True 또는 False (bool)으로 결과 반환
# 찾을 문자열 in 문자열

print("고장" in "설비 고장 발생") # True
print("정상" in "설비 고장 발생") # False
print("설비에서 고장" in "설비 고장 발생") # False
print("설비에서 고장" in "설비에서 고장이 났습니다") # True

# not in - in의 정반대 동작

print("고장" not in "설비 고장 발생") # False
print("정상" not in "설비 고장 발생") # True
print("설비에서 고장" not in "설비 고장 발생") # True
print("설비에서 고장" not in "설비에서 고장이 났습니다") # False

print(" " in "설비 고장 발생") # True

# ==============================

# .count() - 문자열에 특정 글자의 수(int)를 반환
# 문자열.count("찾을 글자")

print("banana".count("a")) # 3
print("010-1234-1234".count("-")) # 2
print("layla@spreatics.com".count("@")) # 1

# ==============================

# find()
# 전달받은 글자가 "첫 번째"로 나오는 위치 인덱스 반환
# 찾는 글자가 없다면 -1을 반환

email = "hong@company.com"
at = email.find("@") # @ 위치의 인덱스인 4가 할당
user_id = email[:at] # hong 이라는 사용자의 아이디만 추출

print(at) # 4
print(user_id) # hong

# SQE-00Q8이라는 설비의 SQE만 뽑아내기 (find와 슬라이싱 사용)
sqe = "SQE-00Q8"

sqe_index = sqe.find("SQE")
print(sqe_index)

sqe_index = sqe.find("-")
print(sqe_index) # 3
sqe_fin = sqe[:sqe_index] # sqe[0:3] -> SQE
print(sqe_fin) # SQE


# ==================================
print("=== index() ===")

# 특정 문자열의 위치(인덱스 번호)를 반환
# 앞에서부터 가장 처음 나오는 인덱스 번호만 반환
# 찾는 문자열이 없으면 Error 발생

email = "layla@spreatics.com"
at = email.index("@") # 5
print(email[0:at]) # layla
print(email[:at]) # 시작 번호가 0이라면 start 생략 가능
print(email[at:]) # 끝까지 출력하고 싶고, 뒤에 몇 글자가 있는지 모르니 생략
# 위처럼 시작하면 5번 인덱스부터 출력하기 때문에 @을 포함
print(email[at+1:]) # at + 1 을 하면 @을 포함하지 않고 출력

# find에서 했던 SQE 뽑아내기 실습 index 사용으로 바꾸기

sqe = "SQE-00Q8"

sqe_index = sqe.index("SQE")
print(sqe_index)

sqe_index = sqe.index("-") # - 있으니 정상 동작
print(sqe_index) # 3
sqe_fin = sqe[:sqe_index] # sqe[0:3] -> SQE
print(sqe_fin) # SQE

# 만약에
# sqe_index = sqe.index("/") # / 없으니 Error 나고 중단됨

# =================================
print("=== count() ===")

# 문자열에서 특정 문자열의 갯수 세기

str11 = "a, b, c, d, e,a, a"

# a의 갯수 세기
print(str11.count("a")) # 3

# ,의 갯수 세기
print(str11.count(",")) # 6

print(str11.count(", ")) # 5 # count로 찾는 문자열과 완전히 동일해야 갯수를 셈

# ========================
print("=== startswith() ===")

# 특정 문자열로 시작하는지 검사
# True/False (불리언)

# EQP로 시작하는지 검사하기
print("EQP-001".startswith("EQP")) # True

# 변수 활용
eqp = "EQP"
print("EQP-001".startswith(eqp)) # True
# 주의사항) 변수명은 따옴표로 감싸기 금지!!!

# ==========================
print("=== endswith() ===")

# 특정 문자열로 끝나는지 확인
# True / False로 반환

str2 = "월요일입니다! 여러분은 할 수 있어요!"

print(str2.endswith("!")) # True
print(str2.endswith("요!")) # True
print(str2.endswith("음!")) # False
print(str2.endswith("월요일입니다! 여러분은 할 수 있어요!")) # True
print(str2.endswith("월요일입니다! 여러분은 할 수 있어요! ")) # False
print(str2.endswith(" 월요일입니다! 여러분은 할 수 있어요!")) # False
# 문자열이 완전 똑같아야만 True가 출력된다.

# ==================================
print("=== 값은 객체다 ===")

print(type("잊어먹으면 안돼!!")) # <class 'str'>
print(len("이렇게 썼죠??")) # 8
# endswith와 len의 차이는?
# endswith는 .으로 연결
  # .으로 연결하는 이런 도구들은 "메서드"
  # 문자열이나 int, float처럼 특정 자료형(객체) 내부에 포함된 기능
# len은 . 사용 안함
  # () -> 함수
  # len과 같이 개발자가 직접 선언하지 않은 기본 제공 함수 "내장함수"
 
"str".startswith("s")
# 123.startswith(1)
# .으로 사용하는 메서드들은 특정 자료형(객체 타입)마다 다름
# int 자료형의 객체에는 startswith라는 메서드가 없음
 
# print(len(123)) # len 내장함수는 길이를 반환하기 때문에 int 자료형 사용 불가

# ========================
# 재할당 복습

num = 1
num = num + 1 # 2
num += 1 # 3
# += 은 복합할당연산자
# 원래 내 자산의 값에 다음 오는 연산자와 값을 적용해서 재할당

# ======================
print("=== .upper() ===")

str3 = "abcdefg"
print(str3) # abcdefg

str3.upper # 반환은 대문자인데, 값에 재할당은 X
print(str3) # abcdefg  # 기존 str3의 값인 소문자를 그대로 출력

# 앞으로 계속 대문자로 변환한 값을 사용하고 싶다면
# 변수에 재할당
# 변수 재할당에서 변수 스스로를 부르는 것이 가능
# 재할당에서 변수 스스로 값을 부르려면 무조건 "재할당"이어야 함
str3 = str3.upper()
print(str3) # ABCDEFG

# str4 = str4.upper() # Error
# 위의 경우 최초 변수 할당 시에는 저장된 값이 없어서
# 변수 스스로 값을 불러와 할당 불가능

# ==============================
user_name = "kim chul soo"

# capitalize는 문자열의 첫 글자만 대문자로 변환
print(user_name.capitalize()) # Kim chul soo

# title은 띄어쓰기 기준으로 각 단어의 첫 글자들을 모두 대문자로 변환
print(user_name.title()) # Kim Chul Soo

# '를 사용한 경우 경우 다른 단어로 인식
print("i'm full".title()) # I'M Full
print("i\'m full".title()) # I'M Full

# ==========================
print("=== .strip() ===")

# 공백 제거
# .strip(): 앞과 뒤의 모든 공백 제거 (중간 띄어쓰기는 그대로 유지)
# .lstrip(): left(왼쪽) 공백만 제거
# .rstrip(): right(오른쪽) 공백만 제거

raw = "   정상   "
print(raw.strip()) # "정상"
print(raw.lstrip()) # "정상   "
print(raw.rstrip()) # "   정상"

# 문자열의 가운데 공백은 strip으로 지우지 못함
print("   정   상   ".strip()) # "정   상"

print(raw) # "   정상   "
# strip은 재할당이나 새 변수에 할당하지 않는 이상 휘발

# strip으로 문자 제거
str4 = "===정상==="
print(str4.strip("=")) # 정상
# 인자로 전달한 양 끝의 =이 모두 제거됨

str5 = "=정상====================="
print(str5.strip("=")) # 정상
# 갯수 상관 없이 인자로 전달한 문자를 무조건 삭제

print(str5.strip("= ")) # wjdtkd
# strip 자체가 공백을 지우는 것이기 때문에
# 공백 상관없이 양 끝의 해당 문자열 삭제

str6 = "==정==상===="
print(str6.strip("=")) # 정==상
# 글자 중간에 있는 문자열은 건드리지 않음

# ==============================
print("=== 체이닝 ===")

raw = "    NORMAL    "
# 체이닝 X
step1 = raw.strip() # "NORMAL"
step2 = step1.lower() # "normal"

# 체이닝 X, 기존 변수에 재할당
raw = raw.strip() # "NORMAL"
raw = raw.lower() # "normal"

# 체이닝 O
chain = raw.strip().lower() # "normal"

# 기존 변수에 재할당도 가능
# raw = rwa.strip().lower()

# 변수에 할당하지 않고 사용 가능
# print(raw.strip().lower()) # "normal"

# strip() 메서드에 인자로 들어가는 문자열은 완전히 동일하지 않아도 전부 삭제
str8 = "aabb 이렇게? cd"
print(str8.strip("abcd ")) # "이렇게?"
print(str8.strip("bc")) # "aabb 이렇게? cd" # 중간에 있는 건 제거 불가

#===============================
print("=== replace() ===")

# 특정 문자열을 제거하거나 치환할 때 사용
# 제거할 때에는 인자의 두 번째를 ""(빈문자열)로 작성
print("정 상 가 동".replace(" ", "")) # 정상가동 (중간 공백 제거)
print("      정              상         가   동   ".replace(" ", "")) # 정상가동

# 글자 치환
print("고장".replace("고장", "fault")) # falut
print("고장".replace("고", "fault")) # falut장

# 단어 치환
str9 = "설비 정상 가동"
print(str9.replace("정상", "점검")) # 설비 점검 가동

# replace() 체이닝
num = "    010-1234-1234    "
num = num.replace(" ", "").replace("-", "") # 01012341234
print(num)

# ==============================
print("=== split() ===")

# 문자열 자르기
# 결고는 대괄호에 감싸진 "리스트" 자료형
# 리스트는 순서가 있기 때문에 왼쪽에서부터 0으로 시작하는 인덱스가 자동 생성

drinks = "에스프레소 아메리카노 카페라떼"
print(drinks.split()) # ['에스프레소', '아메리카노', '카페라떼']
# 띄어쓰기를 기준으로 나뉘어진 세 개의 문자열을 대괄호에 감싸서 반환

# 구분자를 특정하고 싶은 경우
fruits = "딸기,거봉,키위,사쿠란보"
print(fruits.split(",")) # ['딸기', '거봉', '키위', '사쿠란보']
# 무낮열 콤마를 기준으로 분할

fruits2 = "딸기, 거봉, 키위, 사쿠란보"
print(fruits2.split(",")) # ['딸기', ' 거봉', ' 키위', ' 사쿠란보']
# 기준을 콤마로 했기 때문에 공백 그대로 

print(fruits2.split(", ")) # ['딸기', '거봉', '키위', '사쿠란보']
# 문자열 콤마+공백 1칸을 기준으로 분할됨

# 리스트의 인덱스
fruits_list = fruits.split(",")
print(fruits_list) # ['딸기', '거봉', '키위', '사쿠란보']

# 거봉만 출력하기
print(fruits_list[1]) # 거봉
# 출력하고자 하는 요소의 인덱스를 대괄호로 감싸서 호출
print(fruits_list[-1]) # 사쿠란보

# split 횟수 제한
num = "010-1234-1234"
# ["010", "1234-1234"]
print(num.split("-", 1)) # ['010', '1234-1234']

# ========================
print("=== join() ===")
# 리스트를 하나의 문자열로 합침
# "구분자".join(리스트)
# 모든 요소가 합쳐져서 하나의 문자열로 반환

fruits_list = ['딸기', '거봉', '키위', '사쿠란보']

"-".join(fruits_list) # "딸기-거봉-키위-사쿠란보"
",".join(fruits_list) # "딸기,거봉,키위,사쿠란보"
", ".join(fruits_list) # "딸기, 거봉, 키위, 사쿠란보"

# 실습. python 출력하기 - 선생님 방법

word = "python"

# 방법1. strip + capitalize
print(word[:2] + word.strip("py").capitalize()) # pyThon

# 방법2. replace 사용
print(word.replace("t","T")) # pyThon

# 방법3. 슬라이싱 + T만 upper 사용
print(word[:2] + word[2].upper() + word[3:]) # pyThon
      
# 방법4. 인덱싱으로 글자 하나씩 연결
print(word[0] + word[1] + word[2].upper() + word[3] + word[4] + word[5])  # pyThon

# 방법5. 인덱싱 + strip + title
print(word[:2] + word.strip("py").title()) # pyThon

# 방법6. split + join
print(word.split("t")) # ['py', 'hon']
print("T".join(word.split("t"))) # pyThon
print(word[2].upper().join(word.split("t"))) # pyThon

# ==========================
print("=== print 함수의 sep, end ===")

print("2026", "07", "27") # 2026 07 27 (기본적으로는 공백 1칸)

# sep 속성을 사용하면 구분을 공백이 아닌 특정 문자열로 가능
print("2026", "07", "27", sep="사랑해") # 2026사랑해07사랑해27
# 공백 대신 sep 속성에 전달한 문자열이 사빕되어 이어짐

print("안녕", "하세") # 안녕 하세
print("안녕", "하세", end="\n") # 안녕 하세요
# end 속성 사용 시 출력문 마지막에 해당 문자열이 붙어 삽입

# print("안녕", "하세", end="요", "ㅎㅎ") # Error
# end 속성 뒤에 또 인자 넘기기 불가

# print 함수 + 사용 시 sep과 end
print("안녕", "하세", end = "요\n" + "이렇게?") # 안녕 하세요이렇게?
# 정상 동작은 하나, 사용 자제^^ (end를 썼는데 굳이 끝에 +를 사용해 붙이는건 노이해)

# 기본적으로 print문에는 sep으로 공백 한 칸,
# end로 \n(줄바꿈)이 적용되어 있음
# 근데, 개발자가 각 속성을 직접 부여할 경우
# 기본값이 아닌 전달받은 속성값을 사용
print("이런식으로 쓰죠?", "근데 안보이는 기본값이 있어요", sep = " ", end = "\n")

#==================================
print("=== f-string ===")

name = "PUMP_A"
temp = 36

# 출력 결과: 설비 PUMP_A, 온도 36도
# 기존 방법
print("설비 " + name + ", 온도 " + str(temp) + "도") # 설비 PUMP_A, 온도 36도

# f-string 사용
print(f"설비 {name}, 온도 {temp}도") # 설비 PUMP_A, 온도 36도
# 따옴표 밖에 f 작성하기
# 변수면은 꼭 {중괄호}에 감싸기

# f-string 연산
hour = 8

# 우리는 하루에 8시간 수업을 듣고, 이는 480분 입니다.
print(f"우리는 하루에 {hour}시간 수업을 듣고, 이는 {hour * 60}분 입니다.")

# ======================
print("=== f-string 소수 자릿수 ===")

value = 87.456

print(f"{value:.1f} / {value:.2f}") # 87.5 / 87.46

