# 실습 7. 빈도와 그룹 집계 종합
# 빈도 집계와 그룹 집계를 한 흐름으로 연결
# 빈도 집계와 그룹 집계를 한 흐름으로 연결해 분석
import pandas as pd

df = pd.read_csv("data/14_hydraulic.csv", encoding="utf-8")
# df.info()
# 0   냉각기상태   120 non-null    str
#  1   운전부하    120 non-null    str
#  2   밸브상태    120 non-null    str
#  3   온도      120 non-null    float64
#  4   진동      120 non-null    float64
#  5   압력      120 non-null    float64
#  6   냉각효율    120 non-null    float64
#  7   result  120 non-null    str

# · value_counts로 설비 구성과 정상·고장 비율 파악
# 밸브상태별로 비율 확인 - 일단 각 상태별로 몇건이 있는지 확인
# group-size와 다르게 여기는 counts라서 결측(null값) 무시
print(df["result"].value_counts())
# result
# 정상    67
# 고장    53

print(df["result"].value_counts(normalize=True).round(3))
# result
# 정상    0.558
# 고장    0.442

# · 고장 행만 걸러 라인별 고장 건수 집계
# 다음 세가지 방법이 있다. 차이점은 잘 파악해주세요!
# print(len(df[ df['result'] == '고장' ])) # 53 -> 문제에 가장 부합!
# print(df.groupby('result').size()) # 고장    53
# print(df['result'].value_counts()) # 고장    53
# 정상 행만 걸러내기
df_normal = df[df["밸브상태"] == "정상"]
print(len(df_normal))  # 61

# · groupby로 설비별 온도·진동 평균까지 비교
# print(df.groupby('냉각기상태')['온도'].mean().round(2))
# print(df.groupby('냉각기상태')['진동'].mean().round(2))
# 각각 처리하지 말고 한번에!
print(df.groupby(["냉각기상태", "운전부하"])[["온도", "진동"]].mean().round(2))
#                온도    진동
# 냉각기상태 운전부하
# 고장    고부하   55.51  0.73
#       저부하   54.05  0.66
# 저하    고부하   44.07  0.62
#       저부하   45.58  0.61
# 정상    고부하   35.89  0.55
