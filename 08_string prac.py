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
