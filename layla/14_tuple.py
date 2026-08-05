# ===================
# 26.07.31 1교시

tup = ("normal", "normal", "warning", "normal", "warning")
# 길게 쓰고 위 처럼 내리는 방법은, 마지막에 ","를 작성하면 된다.

# # 튜플의 길이
print(len(tup))  # 5

# # 특정 값의 갯수 세기
print(tup.count("warning"))  # 2
# # 찾고자 하는 값이 없으면 "0"이 출력됨

# # 특정 값이 처음 나온 인덱스 찾기
print(tup.index("warning"))  # 2
# # 찾고자 하는 값이 없으면 ValueError 발생

# ============================

# 튜플 리스트
# 리스트 안에 튜플을 담은 것을 표현
# for문으로 리스트를 사용해서 리스트 내부의 튜플에 접근하고
# 튜플에 담긴 값을 사용할 수 있음

# 언패킹을 사용해서 접근한 튜플 내부의 값을
# 변수에 바로 할당해서 접근

hour_13 = [
    ("모터온더", 77),
    ("모터진동", 0.2),
    ("모터압력", 91),
]

now = 0

for name, value in hour_13:
    now += 1
    print(now, "번째 반복")
    print("name:", name, "value:", value)

    # =======

    temps_13 = [
        ("qox_001", 81),
        ("qox_002", 88),
        ("qox_003", 95),
        ("qox_001", 89),
    ]

    warning = 90

    for name, temp in temps_13:
        if temp >= warning:
            print(f"경고 {name} 설비 인상 온도")

# 리스트 안의 튜블 값 갯수가 늘어나면
# for문에서 변수를 여러 개 작성하면 됨


# for문에서도 언배킹 할 때는 무조건 튜플의 값 갯수와
# for문의 변수 갯수 통일
# 통일하지 않을 경우 Error 발생

tup_list = [
    ("일", "one", 1, "1"),
    ("이", "two", 2, "2"),
]

for kor_str, eng_str, num, num_str in tup_list:
    print(f"kor_str {kor_str} eng_str {eng_str} num {num} num_str {num_str}")

# ========================

# 튜플 리스트 정렬
# sorted()를 사용하여
# 튜플의 특정 값 기준으로 리스트를 정렬

temps_13 = [
    (81, "qox_001"),
    (88, "qox_002"),
    (95, "qox_003"),
    (89, "qox_001"),
]

# sorted()는 원본 배열을 수정하지 않고 새 리스트를 반환해줌
hot = sorted(temps_13, reverse=True)
print(hot)
print("원본:", temps_13)  # 정렬 적용 X

# 실습1. 센서를 튜플로 묶고 꺼내기

k = ("모터온도", 80)

print(k)
print(k[0])
print(k[1])

name, value = k
print(name, value)

# 실습2. 튜플 리스트를 반복 처리하기
print("=== 실습2 ===")

s = [("펌프온도", 90), ("모터온도", 88), ("센서온도", 84)]

for name, value in s:
    if value >= 90:
        print(f"{name} 경고")

# 실습3. 중첩 튜플로 센서 위치 관리하기

d = [
    ("ss_501", 50, (6, 2)),
    ("ss_502", 51, (2, 3)),
    ("ss_503", 52, (3, 4)),
]

for name, value, xy in d:
    x, y = xy
    print(name, value, xy)

for name, value, xy in d:
    x, y = xy
    if x <= 5:
        print(name)

