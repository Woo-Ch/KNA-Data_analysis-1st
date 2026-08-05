# int - 정수형
# 소수점 없이 딱 떨어지는 수

count = 3
age = 20
tall = 173


# 0과 음수도 정수에 포함됨
temp = -30
zero = 0

# ========================

# float - 실수
# 소수점이 붙은 숫자
# 5.0처럼 딱 떨어지는 수이지만 소수점이 있다면 무조건 float

tired = 99.99999
height = 17.2

# ========================

# str - 문자열
# 따옴표에 감싸져있는 모든 값

hello = "안녕"
emoji = "❤️"
empty = "" # 따옴표만 있고, 아무것도 작성되지 않아도 str
fake_num = "12345"
fake_num2 = "5.0"
# 아래에서 따옴표가 ""와 '' 둘 다 사용할 수 있는 이유는
# 문자열 안에 따옴표가 필요한 경우가 있기 때문
# 이럴 경우 사용하지 않는 따옴표로 쌍을 맞춰 가장 바깥에 감싸줘야 함
illit = "It's me" 

# =======================

# bool - 불리언형
# True 또는 False만
# 첫 글자는 대문자, 따옴표 없이 작성

ok = True
no = False

# 비교할 경우 bool로 출력
print(100 < 5) # False
print(5 == 5) # True

# =======================

# type() - 자료형 확인
# type(확인하고자 하는 것) > 입력한 것의 자료형을 알려줌

type(5) # 터미널에서 확인 불가 > print하지 않았기 때문

print(type(5)) # <class 'int'>
print(type("센서A")) # <class 'str'>
print(type(True)) # <class 'bool'>
print(type(3 > 2)) # <class 'bool'>
# print 함수의 내부를 확인
# print 함수에 또 함수가 있는 것을 확인하고 type 함수의 내부를 확인
# type 함수의 내부에 연산자가 있는 것을 확인하고 연산 진행
# 3 > 2 의 연산 결과는 True이기 때문에 type(True)로 바뀜
# type(True)의 결과인 <class 'bool'>이 print로 인해 터미널에 출력

print(3, type(3)) # 3 <class 'int'>

num = 123
fake_num = "123"
str = "문자열"
ok = True

# 내가 터미널에서 출력된 결과 중에서
# type()을 사용해서 출력된 자료형을 쉽게 확인할 수 있는 방법
print(num, type(num)) # num <class 'int'>
print(num, ">>>", type(num)) # num >>> <class 'int'>
print(num, ":", type(num)) # num : <class 'int'>

# =======================
print("=== 자료형마다 동작이 다른 것 확인하기 ===")

print(3 + 5) # 8 (int) > 숫자끼리 더하기는 계산
print("3" + "5") # 35 (str) > str끼리 더하기는 이어 붙이기
print("안녕하" + "세요") # 안녕하세요

# =======================
print("=== 자주 하는 실수 ===")

print(0.1 + 0.8) # 0.9
# 가끔 컴퓨터 내부 연산 과정에서 아주 작은 오차가 발생하는 경우도 있음
# 작은 오차 해결법은 round() 사용해서 반올림
print(round(0.1 + 0.8, 2)) # 소수 둘째 자리부터 반올림 # 0.9

# str과 int/float은 덧셈 불가
# print('123' + 456) # TypeError 발생

print(10 / 2) # 5.0 (나눗셈은 결과가 딱 떨어져도 무조건 float)
print(type(10 / 5)) # <class 'float'>
