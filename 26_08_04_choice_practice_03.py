# 실습3. 처리 흐름 만들기


def calc(values):
    avg = sum(values) / len(values)
    return avg


def is_ok(avg):
    if avg >= 80:
        print("정상")
    else:
        print("주의")


temps = [80, 85, 90, 85]

result = calc(temps)

print(f"평균 {result}")
is_ok(result)
