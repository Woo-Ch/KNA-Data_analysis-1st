# =====================================================================
# 종합 실습 1. 설비 종합 모니터링 리포트
# 요구사항 자세히는 practice_guide.md 참고
# =====================================================================

sensors = [
    ("컨베이어_01", 78, 2.1),
    ("용접기_02", 92, 5.4),
    ("절단기_03", 85, 3.2),
    ("건조로_04", 101, 6.8),
    ("냉각탑_05", 67, 1.5),
    ("도장부스_06", 88, 4.1),
    ("성형기_07", 90, 2.9),
]
# (설비명, 온도, 진동)

# 판정 기준
#   온도 > 90 또는 진동 > 5.0  > "위험"
#   온도 >= 80 또는 진동 >= 3.0 > "주의"
#   그 외                      > "정상"

# TODO 1. 각 설비 상태 판정해서 번호 붙여 한 줄씩 출력 (for + enumerate + if/elif/else)

# for no, (name, temp, vib) in enumerate(sensors, start=1):
#     if temp > 90 or vib > 5.0:
#         stat = "위험"
#     elif temp >= 80 or vib >= 3.0:
#         stat = "주의"
#     else:
#         stat = "정상"
#     print(no, name, temp, vib, stat)

# TODO 2. 정상 / 주의 / 위험 각각 몇 대인지 세서 출력 (누적변수)

# print(f"총 설비: {len(sensors)}")

# stats_normal = 0
# stats_warning = 0
# stats_danger = 0
# 누적변수 for문 안에 작성 금지!! -> for문 안에 작성 시 매번 0으로 초기화해버림
# if stats == "정상":
#     stats_normal += 1
# elif stats == "주의":
#     stats_warning += 1
# else:
#     stats_danger += 1

# TODO 3. 이상 설비(주의 + 위험) 비율 % 출력 (round)

# print(
#     f"이상 설비 비율: {(round((stats_warning + stats_danger)/(stats_warning + stats_danger + stats_normal), 1))*100}%"
# )

# TODO 4. 전체 평균 온도 출력 (round)

# temp_sum = 0
# temp_sum += temp
# print(f"평균 온도: {round(((temp_sum)/len(sensors)), 1)}℃")

# TODO 5. 온도 가장 높은 설비 이름 + 온도 출력 (반복문으로 직접 찾기)

# max_temp = 0
# max_name = ""
# if temp > max_temp:
#         max_temp = temp
#         max_name = name
# print(f"최고 온도 설비: {max_name} ({max_temp}℃)")

# TODO 6. "위험" 설비 이름만 모아서 정렬해 리스트로 출력 (.append() + .sort())

# danger_list = []
# danger_list.append(name)
# danger_list.sort()
# print(f"위험 설비 목록: {danger_list}")

# 도전) 위험 1대라도 있으면 "⚠ 즉시 점검 요망", 없으면 "✅ 전 설비 안정"

print("========================================")
print("        설비 종합 모니터링 리포트        ")
print("========================================")
stats_normal = 0
stats_warning = 0
stats_danger = 0

temp_sum = 0

max_temp = 0
max_name = ""

danger_list = []

for no, (name, temp, vib) in enumerate(sensors, start=1):

    if temp > max_temp:
        max_temp = temp
        max_name = name

    temp_sum += temp

    if temp > 90 or vib > 5.0:
        stats = "위험"
        stats_danger += 1
        danger_list.append(name)
    elif temp >= 80 or vib >= 3.0:
        stats = "주의"
        stats_warning += 1
    else:
        stats = "정상"
        stats_normal += 1
    print(no, name, temp, vib, stats)
danger_list.sort()
print("----------------------------------------")
print(f"총 설비: {len(sensors)}")
print(f"정상: {stats_normal} / 주의: {stats_warning} / 위험: {stats_danger}")
print(
    f"이상 설비 비율: {(round((stats_warning + stats_danger)/(stats_warning + stats_danger + stats_normal), 1))*100}%"
)
print(f"평균 온도: {round(((temp_sum)/len(sensors)), 1)}℃")
print(f"최고 온도 설비: {max_name} ({max_temp}℃)")
print(f"위험 설비 목록: {danger_list}")
print("========================================")
