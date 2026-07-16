# 실습. 이름 입력받아 인사 출력

name = input("이름: ")
print("안녕하세요", name+"님!")

# 실습. 숫자 입력받아 계산하기

year_of_birth = int(input("태어난 해: "))
age = 2026 - year_of_birth
print("나이:", age) 

# 실습. 여러 개의 값 입력받기

country = input("거주 국가: ")
city = input("거주 도시: ")
print(country+"의", city+"에서", "거주하시는군요!")

# 실습. 두 수 입력받아 사칙연산

x = int(input("수1: "))
y = int(input("수2: "))
print("두 수의 합:", x + y)
print("두 수의 차:", x - y)

# 실습. 입력값 비교해 출력하기

temp = int(input("온도: "))
print("80도 초과:", temp > 80)
print("0도 이상:", temp >= 0)

# 실습. 입력, 변환, 계산, 비교, 출력 (종합)

# 기준은 60점
a = int(input("점수1: "))
b = int(input("점수2: "))
c = int(input("점수3: "))
print("60점 이상 여부:", (a + b + c) / 3 >= 60)
