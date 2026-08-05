# 실습4. 반환값으로 간단 계산기 만들기


def calc(number_a, number_b):
    total = number_a + number_b
    return total


print(calc(80, 5))  # 85

result = calc(80, 5)

print(result + 5)  # 90
