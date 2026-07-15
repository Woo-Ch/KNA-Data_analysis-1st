# 변수 선언 방법
# 변수이름 = 값
# 오른쪽 값을 왼쪽 이름에 "저장"하라는 코드

temp = 36 # 숫자로 저장하고 싶다면 따옴표 금지
name = "센서 A" # 글자는 무조건 따옴표로 감싸기

print(temp) # 36
print("temp") # temp

# = 은 "같다"가 아니라 "저장"하는 것
# 비교는 == 을 사용

# ======================================
print("==========변수 사용 활용===========")

x = 5
x = x + 5 # 변수를 "재할당"할 때 기존 자신의 값을 활용할 수 있음
#  변수에 할당할 때 오른쪽을 먼저 계산한 뒤 x에 값을 재할당
print(x)

# y = y + 5 # 오류 발생. y가 선언되지 않았기 때문

# ======================================
print("==========재할당===========")

print("재할당하기 전 temp:", temp)
temp = 15 # 위에서 할당했던 36이라는 값을 15로 재할당(수정)
Temp = 150 # temp와 다른 변수로 동작
print("temp:", temp, "Temp:", Temp)

# 재할당은 지금까지 실행된 코드 중 가장 마지막으로 저장된 값이 불려옴
# print(score) # NameError 발생
score = 10
print(score)
score = 20
score = 30
print(score) # 30

print("==========값 복사===========")

a = 10
b = a # b 변수에는 10이 저장 (저장할 때의 그 순간의 a 값을 b에 복사)
a = 100 # a 변수를 재할당해도 b 변수의 값은 10이 그대로 유지
print(b) # 10
print(a) # 100

print("==========여러 변수 한 번에 선언 및 할당===========")

width, height = 10, 20 # width에는 10, height에는 20이 할당됨
print("width:", width, "height:", height)

# 형식: 변수1, 변수2, ... = 값1, 값2, ... -> 변수와 값이 갯수가 같아야 함

# x, y, z = 10, 20 # 변수 3개, 값 2개 실행 시 ValueError가 발생

print("==========주석으로 변수 설명===========")

temp = 25 # 온도(섭씨)
count = 3 # 센서 개수
# temp = 10000000000 # 주석처리된 코드는 동작하지 않음
print(temp) # 25

print("==========실습. 변수 만들고 출력하기===========")

temp = 25
print(temp) # 25
name = "센서A"
print(name) # 센서A

temperature = 30
print(temp) # 30
print(temperature) # 30

my_number = 777
print(my_number)
mood = "최고"
print(mood)

age = 29
label = "나이"
print(label)
print(age)

x = 10
print(x) # 10
x = x + 5
print(x) # 15
x = x * 2
print(x) # 30

a = 100
b = a
a = 999
print(a) # 999
print(b) # 100

print(temp) # NameError
temp = 25
print(temp) # 25
score = 90
# print(Score) # NameError
print(score) # 90

temp = 25 # 온도(섭씨)
count = 3 # 센서 개수
# temp = 100
print(temp) # 25

x = 5
x = 10
x = x + 1
print(x) # 11

name = "나이"
age = 29
print("자기소개")
print(name)
print(age)

# 기존 a = 25
# 기존 b = 3
device_temp = 25 # a를 device_temp로 변경
sensor_count = 3 # b를 sensor_count로 변경
print(device_temp) # 25
print(sensor_count) # 3

x, y, z = 1, 2, 3
width, height = 4, 3
print(x) # 1
print(y) # 2
print(z) # 3
print(width) # 4
print(height) # 3

