# 실습. 설비 정보 출력 카드 만들기

# 출력 결과물
# 설비: PUMP_A
# 상태: 정상
# 가동: 1200
# 점검: 2026-07-16
#
# 삼중따옴표 금지, 이스케이프 문자 사용
# 변수 지정하기
# 가동은 int로 저장

machine = "PUMP_A"
status = "정상"
operate = 1200
inspection = "2026-07-16"

card = "설비: " + machine + "\n상태: " + status + "\n가동: " + str(operate) + "\n점검: " + inspection
print(card)

# 실습. start 생략

word = "temp_sensor"
print(word[:4]) # temp

# 실습. end 생략

word = "temp_sensor"
print(word[5:]) # sensor

# 실습. 음수 슬라이싱

word = "sensor_01"
print(word[-2:]) # 01

# 실습. step으로 건너뛰기

word = "PYTHON"
print(word[::2]) # PTO

# 실습. 문자열 뒤집기

word = "PYTHON"
print(word[::-1]) # NOHTYP

# 실습. len()으로 길이 재기

number = "01012345678"
print(len(number)) # 11

# 실습. .count()로 개수 세기

print("a,b,c,d".count(",")) # 3

# 실습. find에서 했던 SQE 뽑아내기 실습 index 사용으로 바꾸기

sqe = "SQE-00Q8"
sqe_index = sqe.index("-")
sqe_fin = sqe[:sqe_index]
print(sqe_fin) # SQE

# 실습5. 시작과 끝 확인하기

name = "sensor_log.csv"
print(name.startswith("sensor")) # True
print(name.endswith(".csv")) # True

# 실습1. 대문자로 바꾸기
word = "ready"
print(word.upper()) # READY

# 실습2. 소문자로 바꾸기
s = "WARNING"
print(s.lower()) # warning

# 실습3. 단어 첫 글자 대문자로 만들기
name = "kim chul soo"

# 실습4. 대소문자 무시하고 비교하기

# 실습5. 대문자인지 소문자인지 검사하기
word_a = "ABC"
word_b = "abc"
word_c = "Abc"

print(word_a.isupper()) # True
print(word_b.islower()) # True
print(word_c.isupper()) # False

# 실습6. 파일명 규칙 한 번에 점검하기

file_name = "Sensor_LOG.CSV"
file_name_lower = file_name.lower()

print(file_name_lower.startswith("sensor")) # True
print(file_name_lower.endswith(".csv")) # True

# 실습 11. 결과를 변수에 다시 저장하기

str = "    Warning    "
# 1번결과 "    warning    "
str_1 = str.lower()
print("["+str_1+"]") # "[    warning    ]"

# 2번결과 "warning"
str_2 = str.strip().lower()
print("["+str_2+"]") # "[warning]"

# 선생님 정답
str7 = "    Warning    "
str7 = str7.strip()
print("["+str7+"]") # Warning
str7 = str7.lower()
print("["+str7+"]") # warning


# 실습 3. 쉼표 기준으로 나누기
word = "a,b,c,d"
print(word.split(",")) # ['a', 'b', 'c', 'd']

# 실습 5. 리스트 합치기
year = ['2025','01','15']
print("-".join(year)) # 2025-01-15

# 실습
# 변수에 python이라는 문자열 할당
# pyThon 이라고 출력

# 내 방법 1
a = "python"
print(a[:2] + a[2].upper() + a[3:]) # pyThon

 # 내 방법2
a = ['py','t','hon']
a = a[0] + a[1].upper() + a[2]
print("".join(a)) #pyThon

# 실습 7. 구분자 통째로 바꾸기

today = "2026/07/27"
today = today.split("/")
print("-".join(today)) # 2026-07-27

# 실습 8. CSV 한 줄에서 값 꺼내 정리하기

a = "1, NORMAL, 25.3"
a = a.split(",")
print(a[1].strip().lower()) # normal

# 실습1. f-string으로 변수 끼워 출력하기
name = "PUMP_A"
temperature = 87

print(f"설비 {name}, 온도 {temperature}도") # 설비 PUMP_A, 온도 87도