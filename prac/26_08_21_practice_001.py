import pandas as pd

df = pd.read_csv("data/16_diecasting.csv")

# 실습1. 주조 데이터 구조·분포 살펴보기

# 목표
# 주조 데이터를 불러와 크기·컬럼·자료형을 확인


# 단계
# · read_csv로 데이터를 불러와 head로 앞부분 확인
print(df.head())
#  샷  실린더압력    주조압력  사이클타임  비스킷두께    형체력  상태
# 0  1  214.0  1037.0   20.7   10.0  258.0   0
# 1  2  217.0  1052.0   20.7   11.0  257.0   0
# 2  3  214.0  1037.0   20.8   11.0  254.0   0
# 3  4  217.0  1052.0   20.6   11.0  253.0   0
# 4  5  217.0  1052.0   20.6   11.0  254.0   0

# · shape와 columns로 크기와 컬럼 이름 확인
print(df.shape)  # (202, 7)
print(df.columns)
# Index(['샷', '실린더압력', '주조압력', '사이클타임', '비스킷두께', '형체력', '상태'], dtype='str')

# · info로 자료형과 결측 여부 훑기
df.info()
# <class 'pandas.DataFrame'>
# RangeIndex: 202 entries, 0 to 201
# Data columns (total 7 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   샷       202 non-null    int64
#  1   실린더압력   188 non-null    float64
#  2   주조압력    188 non-null    float64
#  3   사이클타임   188 non-null    float64
#  4   비스킷두께   188 non-null    float64
#  5   형체력     188 non-null    float64
#  6   상태      202 non-null    int64
# dtypes: float64(5), int64(2)
# memory usage: 11.2 KB

# 예상 결과
# 202행 7열, 실린더압력·사이클타임 등 컬럼 확인
