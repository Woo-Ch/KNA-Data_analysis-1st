# 실습1 - 여러 자료형 변수

count = 7
temp = 36.5
name = "뉴딜"
is_ok = True
print(count, temp, name, is_ok) # 7 36.5 뉴딜 True

# 실습2 - type()으로 자료형 확인하기

print(type(count)) # <class 'int'>
print(type(temp)) # <class 'float'>
print(type(name)) # <class 'str'>
print(type(is_ok)) # <class 'bool'>

# 실습3 - 자료형 맞히기 퀴즈

print(type(100)) # <class 'int'>  # 정수
print(type(100.0)) # <class 'float'>  # 소수점 - 실수
print(type("100")) # <class 'str'>  # "" - 문자열

# 실습4 - 문자열 숫자와 숫자 비교하기

print(1 + 2) # 3  # 안에 숫자를 계산한 값 출력
print("1" + "2") # 12  # 문자로 인식하여 단순히 붙여서 출력
print("07" + "15") # 0715 # 위와 동일

# 실습5 - bool 값 만들어 확인하기

print(3 > 2) # True
print(5 == 5) # True
print(type(3 > 2)) # <class 'bool'>

# 실습6 - 변수의 자료형 변경하기

age = 29
print(type(age)) # <class 'int'>
age = 29.0
print(type(age)) # <class 'float'>
age = "29"
print(type(age)) # <class 'str'>

# 실습7 - 직접 자료형 표현하기

device_temp = 36.5 # float
check_count = 7 # int
device_name = "K뉴딜" # str
is_normal = false # bool
