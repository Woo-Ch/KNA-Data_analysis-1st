# 실습1. value_counts로빈도세기
# 한 열을 골라 value_counts로 값별 개수 세기
import pandas as pd

# 목표
# 한 열의 값별 개수를 세어 데이터 구성 파악

# 단계
# · 설비 데이터를 불러와 앞부분과 구조 확인
df = pd.read_csv("data/14_hydraulic.csv", encoding="utf-8")
df.info()

# · 설비 열에 value_counts를 붙여 값별 개수 세기
print(df["냉각기상태"].value_counts())
# 냉각기상태
# 고장    40
# 저하    40
# 정상    40
# Name: count, dtype: int64

# · 교대 열도 같은 방법으로 세어 가장 많은 값 확인
print(df["운전부하"].value_counts())
# 운전부하
# 고부하    60
# 저부하    60
