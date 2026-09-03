import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)

tags = pd.read_csv("Allie/03-01_회전기계_신호_회전기계태그목록.csv")
df = pd.read_csv("Allie/03-01_회전기계_신호_진동추세.csv")

# 1번 모터에 대한 태그 목록
print(
    tags.loc[tags["equipment"] == "1번 모터"],
    ["tag", "indicator", "summary", "unit", " direction"],
)

# 진동의 정상 범위 정하기
# 맨 앞 기준으로 20일 구간을 정상 기간으로 볼 것

MTR = ["MTR01_VIB_H", "MTR01_VIB_V", "MTR01_VIB_A", "MTR01_VIB_ACC"]
normal = df.head(20)

print(normal[MTR].agg(["min", "max"]))

# 펌프 극단값 출력해보기
PMP = ["PMP01_VIB_H", "PMP01_VIB_V", "PMP01_VIB_A", "PMP01_VIB_ACC"]
print(df[PMP].agg(["min", "max"]))

print("==============2교시==============")


def first_over(col):
    "정상 구간 최댓값을 처음 넘어선 행의 순서를 반환합니다."
    limit = normal[col].max()  # 20일 구간(normal)의 최댓값을 정상 범위로 설정
    over = df.index[df[col] > limit]  # 정상 범위를 넘는 index를 불러온다.

    return int(over[0]) + 1 if len(over) else None


print("1번 모터")
for c in MTR:
    print(f"{c} : {first_over(c)}일차에 정상 범위를 벗어남")

for c in PMP:
    print(f"{c} : {first_over(c)}일차에 정상 범위를 벗어남")

for c in ["MTR01_CURRENT", "MTR01_TEMP"]:
    print(f"{c} : {first_over(c)}일차에 정상 범위를 벗어남")

# 모터 1번의 회전수
# 모터 1번 회전수의 컬럼 이름
# 1780, 1450 종류의 숫자가 각각 몇 번 찍히는지
print(df["MTR01_RPM"].value_counts())
# 1780    56
# 1450     4

print(
    df.loc[
        df["MTR01_RPM"] == 1780, ["date", "MTR01_VIB_H", "MTR01_VIB_ACC", "MTR01_RPM"]
    ].head(4)
)
print(
    df.loc[
        df["MTR01_RPM"] == 1450, ["date", "MTR01_VIB_H", "MTR01_VIB_ACC", "MTR01_RPM"]
    ]
)

# date  MTR01_VIB_H  MTR01_VIB_ACC  MTR01_RPM
# 0  2026-01-01          1.8           0.52       1780
# 1  2026-01-02          1.9           0.54       1780
# 2  2026-01-03          1.8           0.53       1780
# 3  2026-01-04          2.0           0.55       1780
#           date  MTR01_VIB_H  MTR01_VIB_ACC  MTR01_RPM
# 29  2026-01-30          1.3           0.61       1450
# 30  2026-01-31          1.3           0.63       1450
# 31  2026-02-01          1.4           0.67       1450
# 32  2026-02-02          1.3           0.68       1450

print("==============실습1.==============")
# 실습1. 회전기계 데이터셋 컬럼 매핑
# - 케이스 A : 1번 모터 - 베어링 손상 조기 경보
# - 케이스 B : 1번 팬 - 분진 축적에 따른 불평형 감지

# ======= CASE A =======
# [Step 1] 고장 유형과 물리량 도출

#  목표 고장 유형 : 1번 모터 - 베어링 손상 조기 경보
#  진행 속도 (빠름 / 느림) : ____________

#  구분        | 물리량 | 그 물리량을 고른 이유
# ------------|-------|--------------------------------
#  주 신호     |       |
#  확인 신호 1 |       |
#  확인 신호 2 |       |

col2 = ["MTR01_VIB_H", "MTR01_VIB_V", "MTR01_VIB_A", "MTR01_VIB_ACC"]
print(df[col2].agg(["min", "max"]))
print(df[col2].diff().head(10))
