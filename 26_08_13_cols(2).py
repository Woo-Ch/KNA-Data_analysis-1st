# 복수 열 선택
import pandas as pd

df = pd.read_csv("data/13_diecasting_small.csv")
df.info()
# <class 'pandas.DataFrame'>
# RangeIndex: 30 entries, 0 to 29
# Data columns (total 7 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   샷       30 non-null     int64
#  1   실린더압력   30 non-null     float64
#  2   주조압력    30 non-null     float64
#  3   사이클타임   30 non-null     float64
#  4   비스킷두께   30 non-null     float64
#  5   형체력     30 non-null     float64
#  6   품질등급    30 non-null     str
# dtypes: float64(5), int64(1), str(1)
# memory usage: 1.8 KB

df["형체력"].info()  # Series
# <class 'pandas.Series'>
# RangeIndex: 30 entries, 0 to 29
# Series name: 형체력
# Non-Null Count  Dtype
# --------------  -----
# 30 non-null     float64
# dtypes: float64(1)
# memory usage: 372.0 bytes

# df["형체력", "실린더입력"].info() # KeyError

df[["형체력", "실린더압력"]].info()  # DataFrame
# <class 'pandas.DataFrame'>
# RangeIndex: 30 entries, 0 to 29
# Data columns (total 2 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   형체력     30 non-null     float64
#  1   실린더압력   30 non-null     float64
# dtypes: float64(2)
# memory usage: 612.0 bytes
