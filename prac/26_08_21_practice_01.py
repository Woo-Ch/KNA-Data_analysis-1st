import pandas as pd

df = pd.read_csv("data/15_02_사출성형_공정.csv", encoding="utf-8")
df.info()
# <class 'pandas.DataFrame'>
# RangeIndex: 250 entries, 0 to 249
# Data columns (total 22 columns):
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
#  20  최대사출속도  141 non-null    float64
#  21  감압시간    141 non-null    float64
# dtypes: float64(19), int64(1), str(2)
# memory usage: 43.1 KB

# 실습 1. dropna로 행·열 삭제
# 결측 있는 행과 열을 삭제하고 크기 변화 확인
# 결측 있는 행과 열을 삭제하고 크기 변화 확인

# · 원본 크기를 shape로 확인
print(df.shape)  # (250, 22)

# · dropna로 결측 있는 행을 모두 삭제
print(df.dropna().shape)  # (76, 22)

# · 방향을 열로 바꿔 결측 있는 열을 삭제
print(df.dropna(axis=1).shape)  # (250, 10)

# 예상 결과
# 250×22 → 행삭제 76×22, 열삭제 250×10
