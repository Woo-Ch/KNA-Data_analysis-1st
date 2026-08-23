import pandas as pd

df = pd.read_csv("data/15_02_사출성형_공정.csv", encoding="utf-8")
# 실습 8. 제거 vs 대체 비교
# 같은 데이터에 제거와 대체를 적용해 결과 비교

# · 결측 심한 컬럼을 먼저 뺀 기준 데이터 만들기
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
기준 = df.drop(columns=["최대사출속도", "감압시간"])
기준.info()  # 최대사출속도, 감압시간 컬럼 제거 확인
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
print(기준.shape)  # (250, 20)

print("=" * 40)
# · 기준 데이터에서 결측 행을 삭제한 제거 버전 만들기
제거판 = 기준.dropna()
print(제거판.shape)  # (110, 20)

# · 기준 데이터의 결측을 중앙값으로 채운 대체 버전 만들기
대체판 = 기준.fillna(기준.median(numeric_only=True))
# (numeric_only=True) 는 숫자만 계산함을 의미
print(대체판.shape)  # (250, 20)

# 예상 결과
# 제거 버전 110행, 대체 버전 250행(모두 유지)
