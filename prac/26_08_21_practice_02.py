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

# 실습 2. dropna 옵션 조절
# how·thresh·subset로 삭제 기준을 세밀하게 조절

# · how로 완전히 빈 행만 삭제하는 기준 적용 -> how = 'all'
print(df.dropna(how="all").shape)  # (250, 22)
# 250개 row가 다 살아남았다는 의미
# : NaN으로 모든 컬럼 내용이 다 채워진 row가 없다는 뜻

# · thresh로 값이 일정(예, 20개) 개수 "이상"인 행만 남기기 -> thresh = 20
print(df.dropna(thresh=20).shape)  # (162, 22)
# 250 - 162 = 88개 row는 NaN이 3개 이상이라는 뜻

# · subset으로 특정 컬럼이 빈 행만 삭제
# 예, 불량여부 컬럼에 NaN이 있는 row들만 제거 -> subset = ['불량여부']
print(df.dropna(subset=["불량여부"]).shape)  # (250, 22)
# '불량여부' 컬럼에는 NaN이 하나도 없다고 판단 가능

# 예상 결과
# 완전 결측 행만 삭제는 거의 유지, 임계값 20은 162행
