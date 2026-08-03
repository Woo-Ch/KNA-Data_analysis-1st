print("===== 실습2 ======")
# 실습2. update로 여러 값 한 번에 갱신하기

sensors = {"모터온도": 80, "진동": 1.5}
new_data = {"모터온도": 90, "압력": 30}

print(sensors)  # {'모터온도': 80, '진동': 1.5}

sensors.update(new_data)
print(sensors)  # {'모터온도': 90, '진동': 1.5, '압력': 30}

del sensors["모터온도"]
print(sensors)  # {'진동': 1.5, '압력': 30}

print(len(sensors))  # 2


print("===== 실습3 ======")
# 실습3. 딕셔너리로 통계 내기
sensors = {"압력": 60, "압력2": 70, "압력3": 80, "압력4": 90}
print(sensors)

sensors_avg = sum(sensors.values()) / len(sensors)
print(f"평균: {sensors_avg}")

for name, value in sensors.items():
    if value == max(sensors.values()):
        print(f"최댓값 센서: {name} {value}")


print("===== 실습4 =====")
# 실습4. zip으로 센서명-값 매핑하기

sensors = ["온도", "압력", "진동"]
values = [70, 50, 1.5]

sensors_values = dict(zip(sensors, values))
print(sensors_values)

for name, value in sensors_values.items():
    print(name, value)


print("===== 실습5 =====")
# 실습5. 임계값으로 경고 센서 분류하기

# 측정값
value_real = {"온도": 70, "진동": 3}
# 임계값
value_warning = {"온도": 65, "진동": 4}

for name, value in value_real.items():
    if value > value_warning[name]:
        print(f"경고센서: ['{name}']")


print("===== 실습6 =====")
# 실습6. 중첩 딕셔너리로 설비 관리하기

machine = {
    "보일러": {"온도": 80, "진동": 2.5, "압력": 30, "상태": "정상"},
    "유압장치": {"온도": 90, "진동": 1.5, "압력": 25, "상태": "경고"},
}

print(machine["보일러"]["온도"])  # 80

for name, info in machine.items():
    if info["상태"] == "경고":
        print(f"{name} 점검 필요")


print("===== 실습8 =====")
# 실습8. 센서 데이터 통합 정리

# 측정값
value_real = {"온도": 70, "진동": 3, "압력": 30}
# 임계값
value_warning = {"온도": 65, "진동": 4, "압력": 20}

avg = sum(value_real.values()) / len(value_real)
print(f"평균: {avg}")

danger = set()

for name, value in value_real.items():
    if value > value_warning[name]:
        danger.add(name)

print(f"위험센서: {danger}")
