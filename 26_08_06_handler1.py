# 트레이스백으로 에러 읽기

# ValueError: 글자를 숫자로 변환 요구 - 당연히 실패
# temp = int("스물")
# print(temp) # ValueError

# 정상화
temp = int("20")
print(temp)  # 20

print("=" * 30)

# ZeroDivisionError: 숫자는 0으로 나눌 수 없어요
# result = 10 / 0
# print(result)

# 정상화
result = 10 / 2
print(result)  # 5.0

print("=" * 30)

# NameError -: 그런 이름도 있었어요?라는 뜻의 에러
# hello()

# 정상화
print("hello")  # hello

