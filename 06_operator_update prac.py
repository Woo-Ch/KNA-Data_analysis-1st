# 실습1. 사칙연산 계산기, 기초

a = 17
b = 5

print(a + b) # 22
print(a - b) # 12
print(a * b) # 85
print(a / b) # 3.4
print(a // b) # 3
print(a % b) # 2
print(a ** b) # 1419857


# 실습2. 평균과 도형 계산, 응용

# 평균 구하기
q = 10
w = 20
e = 30
print((q + w + e) / 3) # 20.0
# 넓이 구하기 = 변 ** 2
side = 5
print(side ** 2) # 25
# 부피 구하기 = 가로 * 세로 * 높이
x = 1
y = 2
z = 3
print(x * y * z) # 6

# 실습3. 비교 연산 출력
print(1 == 1) # True
print(1 != 2) # True
print(2 > 3) # False
print(2 < 3) # True
print(1 >= 1) # True 
print(3 <= 2) # False

# 실습4. 정상범위, 다중센서 판정, 실전

temp = 85
temp_status = temp >= 50 and temp <= 90
print(temp_status) # True
pressure = 5
pressure_status = pressure >= 3 and pressure <= 7
print(pressure_status) # True
print(temp_status and pressure_status) # True

# 실습5. 복합 할당으로 재고 추적, 기초

stock = 100
print(stock) # 100
stock += 50
print(stock) # 150
stock -= 30
print(stock) # 120
stock += 5
print(stock) # 125

# 실습6. 설비 지표 계산, 실전

total = 500
bad = 23
print((bad/total) * 100, "%") # 4.6 %
operate = 21
total_operate = 24
print((operate/total_operate) * 100, "%") # 87.5 %

# 실습7. 시간 변환, 상자 포장, 도전

minutes = 500
print((minutes//60), ":", (minutes%60)) # 8 : 20
print((minutes//60), "시간", (minutes%60), "분") # 8 시간 20 분
