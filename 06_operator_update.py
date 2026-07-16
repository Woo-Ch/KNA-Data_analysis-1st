# 산술연산자
# +, -, *, /, //(몫), %(나머지), **(거듭제곱)

print(3 + 5) # 8
print(10 - 4) # 6
print(4 * 5) # 20
print(20 / 4) # 5.0 (나눗셈 결과는 항상 float)
print(7 // 3) # 2 (몫)
print(7 % 3) # 1 (나머지)
print(2 ** 5) # 32 (거듭제곱, 2의 5제곱)

# ==============================
# 연산 우선순위와 우선순위 지정
# 연산 우선순위: ** > * / // % > + -

print(2 + 8 * 3) # 26
print((2 + 8) * 3) # 30

# ==============================
# 복합연산자

result = 3 * 5
print(result) # 15

# += : 기존 값에서 오른쪽 값을 더한 뒤 재할당
# -= : 기존 값에서 오른쪽 값을 뺀 뒤 재할당
# *= : 기존 값에서 오른쪽 값을 곱한 뒤 재할당
# /= : 기존 값에서 오른쪽 값을 나눈 뒤 재할당

result += 10 # 25
print(result) # 25
result -= 5 # 20
print(result) # 20
result *= 3 # 60
print(result) # 60
result /= 2 # 30
print(result) # 30.0

# ==============================
# 문자열 연산

print("안녕" + "하세요") # 안녕하세요

# 만약 "안녕" 과 "하세요" 사이에 공백 1개 넣고 싶다면
# 방법 1) , 사용
print("안녕", "하세요")

# 방법 2) 안녕 뒤에 공백 추가
print("안녕 " + "하세요")

# 방법 3) 공백만 있는 문자열 더하기
print("안녕" + " " + "하세요")

# 문자열 곱하기
print("안녕" * 5) # 안녕안녕안녕안녕안녕

# 문자열에 연산자를 사용할 경우 모두 이어져서 나옴


# ==============================
print("=== 비교연산자 ===")

# <(미만), <(초과), <=(이하), >=(이상), ==(같다), !=(다르다)
# 비교 결과는 무조건 True or False (bool)

print(7 < 16) # True
print(7 > 16) # False
print(7 <= 7) # True
print(7 >= 7) # True
print(7 == 7) # True
print(7 != 7) # False

# 비교연산자는 문자열 비교도 가능
print("hello" == "hello") # True
print("정상" == "정상") # True

# 비교연산자를 사용해 문자열을 비교할 때 주의사항

# 1. 대소문자 구분
print("hello" == "Hello") # False

# 2. 공백이 있어도 다르다고 판단
print("정상" == "정상 ") # False

# 부정연산자 != (not)
print("hello" != "hello") # False (!=는 다르다는 의미 이기 때문에 False가 출력)
print("hello" != "hello ") # True (띄어쓰기로 인해 다르기 때문에 True 출력)
print("hello" != "Hello") # True

# 질문 1) hello 변수에 할당하는 값을 따옴표로 감싸지 않고 비교
# print("=== 질문 1) hello 변수에 할당하는 값을 따옴표로 감싸지 않고 비교 ===")
# hello = hi
# print(hello == hi)  # NameError(선언하지 않은 이름 호출했을 때)
# hi는 따옴표에 감싸져있지 않기 때문에 변수로 취급됨
# 그런데 우리는 hi 변수를 선언한 적이 없기 때문에 에러

# 질문 1) 해결방법
# print("=== 질문 1) 해결 방법 ===")
hi = "안녕"  # hello 변수에 hi 변수를 할당하기 전 hi 변수 선언
hello = hi  # print(hello) > 안녕
print("=== 변수 hello(안녕)와 변수 hi(안녕) 비교 ===")
print(hello == hi)  # True

# =================================

# and / or / not - 논리연산자
# and: 둘 다 True여야 True를 반환
print(5 == 5 and 7 == 7) # True + True = True
# and는 첫 번째 조건이 False라면 뒤에 조건은 확인 안함
print(5 == 7 and 7 == 7) # False + True = False
print(5 == 5 and 7 != 7) # True + False = False
# 위 코드는 가능하다면 7 != 7 and 5 == 5 순서로 작성

#or: 하나라도 True라면 True 반환   
print(5 == 5 or 7 == 7) # True + True = True
print(5 == 7 or 7 == 7) # False + True = True
# or는 첫 번째 조건이 True라면 뒤에 조건은 확인 안함
print(5 == 5 or 7 != 7) # True + False = True

# not: 값을 반대로 뒤집음
print(not True) #False
print(not 5 == 5) # false
# 5 == 5를 연산하여 True를 반환
# not True로 동작해서 True를 뒤집어 False 반환
# 반환받은 False라는 값을 print가 터미널로 출력
