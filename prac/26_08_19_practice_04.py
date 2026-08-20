# 실습4. groupby로 그룹 집계

import pandas as pd

df = pd.read_csv("data/14_hydraulic.csv", encoding="utf-8")
df.info()
# 0   냉각기상태   120 non-null    str
#  1   운전부하    120 non-null    str
#  2   밸브상태    120 non-null    str
#  3   온도      120 non-null    float64
#  4   진동      120 non-null    float64
#  5   압력      120 non-null    float64
#  6   냉각효율    120 non-null    float64
#  7   result  120 non-null    str

# 실습 4. groupby로 그룹 집계
# 기준 → 열 → 함수 순으로 그룹별 통계 구하기
# 기준 열로 그룹을 나눠 그룹별 통계 구하기

# · 라인으로 그룹을 나눠 압력 열의 평균 집계
# 운전부하별 압력 평균
print(df.groupby("운전부하")["압력"].mean().round(2))
# 운전부하
# 고부하    164.12
# 저부하    157.88

# · 집계 함수를 바꿔 설비별 최고 온도 확인 - max, min
# 운전부하에서 벨브상태별로 최고 온도
print(df.groupby(["운전부하", "밸브상태"])["온도"].max())
# 운전부하  밸브상태
# 고부하   경미      57.1
#       심각      57.6
#       정상      57.8
#       지연      57.5
# 저부하   경미      55.0
#       심각      54.6
#       정상      57.1
#       지연      56.6

# · size로 교대별 측정 건수까지 확인
# 운전부하별로 size로 갯수 세기 (결측-null값 갯수도 포함)
print(df.groupby("운전부하").size())
# 운전부하
# 고부하    60
# 저부하    60
