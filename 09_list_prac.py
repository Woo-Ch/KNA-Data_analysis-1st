# 실습1. 나만의 데이터 리스트 만들기

today = [34, 35, 36, 37, 38]
print(today) # [34, 35, 36, 37, 38]

print(len(today)) # 5

empty = []
print(len(empty)) # 0

# 실습2. 인덱스로 값 꺼내기

today = [34, 35, 36, 37, 38, 39]

print(today[0]) # 34
print(today[2]) # 36
print(today[-1]) # 39

# 실습3. 인덱스로 꺼낸 값 계산하기

a = [10, 20, 30, 40, 50, 60]
a_1 = a[0]
a_last = a[-1]
print(a_1 + a_last) # 70
print((a_1 + a_last)/2) # 35.0

# 실습4. 슬라이싱으로 구간 자르기

b = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
print(b[:3]) # [31, 32, 33]
print(b[-3:]) # [38, 39, 40]
print(len(b[:3])) # 3

# 실습5. 데이터를 두 구간으로 나누기

c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
first = c[:6]
print(first) # [1, 2, 3, 4, 5, 6]
second = c[-6:]
print(second) # [1, 2, 3, 4, 5, 6]

print(len(first)) # 6
print(len(second)) # 6

# 실습6. 값 찾아 바꾸기

d = [25, 26, 240, 28, 27]
print(25 in d) # True
print(26 in d) # True
print(24 in d) # False
print(28 in d) # True
print(27 in d) # True

print(d.index(240)) # 2
d = [25, 26, 24, 28, 27]

print(d) # [25, 26, 24, 28, 27]
print(24 in d) # True

# 실습7. 측정값 추가하기

f = []
f.append(30)
print(f) # [30]
f.insert(0, 28)
print(f) # [28, 30]

f_second = [31, 32]
f.extend(f_second)
print(f) # [28, 30, 31, 32]

# 실습8. 잘못된 값 제거하기

a = [25, 26, 24, 28, 26, 999]

print(a) # [25, 26, 24, 28, 26, 999]
a.remove(999)
print(a) # [25, 26, 24, 28, 26]

print("꺼낸 값", a.pop(1)) # 꺼낸 값 26

del a[0]
print(a) # [24, 28, 26]

# 실습9. 정렬하고 탐색하기

temp = [24, 22, 24, 26, 28, 27, 30]
temp.sort()
print(temp) # [22, 24, 24, 26, 27, 28, 30]

temp.reverse()
print(temp) # [30, 28, 27, 26, 24, 24, 22]

print(temp.count(24)) # 2

print(temp.index(30)) # 0
