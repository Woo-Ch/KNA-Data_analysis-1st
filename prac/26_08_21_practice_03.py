import pandas as pd

df = pd.read_csv("data/15_02_사출성형_공정.csv", encoding="utf-8")
print(df.shape)  # (250, 22)
print(df.isna().sum())
# 측정시각        0
# 불량여부        0
# 사출기         0
# 사이클시간       0
# 성형사이클       0
# 배럴온도1       0
# 배럴온도2       0
# 배럴온도3       0
# 배럴온도4       0
# 호퍼온도        0
# 스크루속도       1
# 사출압력        3
# 스크루위치       5
# 전환위치        9
# 계량시간        9
# 계량시작위치     34
# 계량시작점      34
# 최소쿠션       34
# 최대사출압      60
# 전환압력       68
# 최대사출속도    109
# 감압시간      109
# dtype: int64

print("=" * 40)
# 실습 3. 결측 비율 기준 컬럼 제거
# 결측 비율이 높은 컬럼만 골라 제거

# 단계
# · 컬럼별 결측 비율을 계산
df_rate = df.isna().sum() / len(df)
print(df_rate)
# 측정시각      0.000
# 불량여부      0.000
# 사출기       0.000
# 사이클시간     0.000
# 성형사이클     0.000
# 배럴온도1     0.000
# 배럴온도2     0.000
# 배럴온도3     0.000
# 배럴온도4     0.000
# 호퍼온도      0.000
# 스크루속도     0.004
# 사출압력      0.012
# 스크루위치     0.020
# 전환위치      0.036
# 계량시간      0.036
# 계량시작위치    0.136
# 계량시작점     0.136
# 최소쿠션      0.136
# 최대사출압     0.240
# 전환압력      0.272
# 최대사출속도    0.436
# 감압시간      0.436
# dtype: float64

print("=" * 40)
# · 비율이 기준을 넘는 컬럼 이름만 목록으로 뽑기
# -> 40% 이상 NaN으로 채워진 컬럼 목록
df_terminates = df_rate[df_rate > 0.4]
print(df_terminates)
# 최대사출속도    0.436
# 감압시간      0.436

print("=" * 40)
# 최초 컬럼 이름들이 df_terminates의 index labels가 되었다.
list_terminates = df_terminates.index.tolist()
# df_terminates의 행 인덱스 가져오고, tolist로 리스트화
print(list_terminates)  # ['최대사출속도', '감압시간']

print("=" * 40)
# · 그 컬럼들을 drop으로 제거하고 크기 확인
# drop에 컬럼을 제시하면 기본동작 : 컬럼을 지워버림
df_final = df.drop(columns=list_terminates)
df_final.info()
# <class 'pandas.DataFrame'>
# RangeIndex: 250 entries, 0 to 249
# Data columns (total 20 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   측정시각    250 non-null    str
#  1   불량여부    250 non-null    int64
#  2   사출기     250 non-null    str
#  3   사이클시간   250 non-null    float64
#  4   성형사이클   250 non-null    float64
#  5   배럴온도1   250 non-null    float64
#  6   배럴온도2   250 non-null    float64
#  7   배럴온도3   250 non-null    float64
#  8   배럴온도4   250 non-null    float64
#  9   호퍼온도    250 non-null    float64
#  10  스크루속도   249 non-null    float64
#  11  사출압력    247 non-null    float64
#  12  스크루위치   245 non-null    float64
#  13  전환위치    241 non-null    float64
#  14  계량시간    241 non-null    float64
#  15  계량시작위치  216 non-null    float64
#  16  계량시작점   216 non-null    float64
#  17  최소쿠션    216 non-null    float64
#  18  최대사출압   190 non-null    float64
#  19  전환압력    182 non-null    float64
# dtypes: float64(17), int64(1), str(2)
# memory usage: 39.2 KB

# 예상 결과
# 40% 초과 센서19·20 제거 → 250×20
print(df_final.shape)  # (250, 20)
