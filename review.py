# 26.07.28 학습내용 복습

## f-string과 텍스트 pdf

# 실습1. f-string으로 변수 끼워 출력하기
name = "PUMP_A"
temp = 87

print(f"설비 {name}, 온도 {temp}도") # 설비 PUMP_A, 온도 87도

# 실습2. f-string 안에서 계산하기
a = 80
b = 90
c = 100

print(f"평균 {(a+b+c)/3}") # 평균 90.0

# 실습3. 소수점 자릿수 지정하기
a = 87.456

print(f"{a:.1f}") # 87.5
print(f"{a:.2f}") # 87.46

# 실습4. 센서 로그 한 줄 정리 리포트 만들기
x = " 5, sensor_2, WARNING, 0.78912 "

x = x.strip().split(",")

sensor = x[1].strip()
stats = x[2].strip().lower()
measurements = float(x[3].strip())

print(f"[센서 {sensor}] 상태 {stats}, 측정값 {measurements:.2f}")

## 리스트 pdf

# 실습1. 나만의 데이터 리스트 만들기
a = [30, 31, 32, 33, 34]

print(a) # [30, 31, 32, 33, 34]
print(len(a)) # 5

b = []
print(len(b)) # 0

# 실습2. 인덱스로 값 꺼내기
a = [30, 31, 32, 33, 34, 35]

print(a[0]) # 30
print(a[2]) # 32
print(a[-1]) # 35

# 실습3. 인덱스로 꺼낸 값 계산하기
a = [10, 20, 30, 40, 50, 60]

a_first = a[0]
a_last = a[-1]

print(a_first + a_last) # 70
print((a_first + a_last) / 2) # 35.0

# 실습4. 슬라이싱으로 구간 자르기
a = [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]

print(a[:3]) # [30, 31, 32]
print(a[-3:]) # [39, 40, 41]
print(len(a[:3])) # 3

# 실습5. 데이터를 두 구간으로 나누기
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

first = a[:6]
second = a[-6:]

print(first) # [1, 2, 3, 4, 5, 6]
print(second) # [7, 8, 9, 10, 11, 12]

print(len(first)) # 6
print(len(second)) # 6

# 실습6. 값 찾아 바꾸기
temp = [25, 26, 240, 28, 27]

print(240 in temp) # True

print(temp.index(240)) # 2

temp = [25, 26, 24, 28, 27]
print(temp) # [25, 26, 24, 28, 27]

# 실습7. 측정값 추가하기
a = []

a.append(30)
print(a) # [30]

a.insert(0, 28)
print(a) # [28, 30]

b = [31, 32]
a.extend(b)
print(a) # [28, 30, 31, 32]

# 실습8. 잘못된 값 제거하기
a = [25, 26, 24, 28, 26, 999]

a.remove(999)
print(a) # [25, 26, 24, 28, 26]

a.pop(1)

del a[0]
print(a) # [24, 28, 26]

# 실습9. 정렬하고 탐색하기
