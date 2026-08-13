# 실습8. 압축기와 디지털 신호 구조 비교
# shape, info, describe

import pandas as pd

df_compressor = pd.read_csv("data/12_metro_compressor.csv")
print(df_compressor.shape)  # (200, 7)

df_compressor.info()
# <class 'pandas.DataFrame'>
# RangeIndex: 200 entries, 0 to 199
# Data columns (total 7 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   측정시각    200 non-null    str
#  1   압축압력    200 non-null    float64
#  2   배출압력    200 non-null    float64
#  3   저장압력    200 non-null    float64
#  4   오일온도    199 non-null    float64
#  5   모터전류    200 non-null    float64
#  6   가동상태    200 non-null    str
# dtypes: float64(5), str(2)
# memory usage: 11.1 KB

print(df_compressor.describe())
# 압축압력        배출압력  ...        오일온도        모터전류
# count  200.000000  200.000000  ...  199.000000  200.000000
# mean     9.172200   -0.016950  ...   63.181910    2.060850
# std      0.583699    0.047173  ...    6.249822    2.196505
# min      8.130000   -0.030000  ...   50.100000    0.030000
# 25%      8.700000   -0.020000  ...   58.100000    0.040000
# 50%      9.175000   -0.020000  ...   62.900000    0.040000
# 75%      9.665000   -0.020000  ...   68.100000    3.812500
# max     10.220000    0.600000  ...   75.000000    6.190000

df_digital = pd.read_csv("data/12_metro_digital.csv")
print(df_digital.shape)  # (120, 4)

df_digital.info()
# <class 'pandas.DataFrame'>
# RangeIndex: 120 entries, 0 to 119
# Data columns (total 4 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   측정시각    120 non-null    str
#  1   압축기     120 non-null    int64
#  2   타워      120 non-null    int64
#  3   저압스위치   120 non-null    int64
# dtypes: int64(3), str(1)
# memory usage: 3.9 KB

print(df_digital.describe())
# 압축기          타워  저압스위치
# count  120.000000  120.000000  120.0
# mean     0.908333    0.933333    0.0
# std      0.289765    0.250490    0.0
# min      0.000000    0.000000    0.0
# 25%      1.000000    1.000000    0.0
# 50%      1.000000    1.000000    0.0
# 75%      1.000000    1.000000    0.0
# max      1.000000    1.000000    0.0
