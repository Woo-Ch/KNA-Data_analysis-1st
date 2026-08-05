# 선택5. 센서 통계 함수 만들기


def calc(values):
    minimum = min(values)
    maximum = max(values)
    avg = sum(values) / len(values)
    return minimum, maximum, avg


temps = [78, 85, 92, 85]

calc_min_max_avg = calc(temps)

print(calc_min_max_avg)  # (78, 92, 85.0)
