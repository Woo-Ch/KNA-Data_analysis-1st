# loc 행과 열

import pandas as pd

df = pd.read_csv("data/13_diecasting_small.csv")
df.info()

print("=" * 30)

df.loc[0].info()  # Series

# 행 언급 서브 DF 만들기
df_sub = df.loc[0:2]
df_sub.info()  # DataFrame
print(df_sub)
# #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   샷       3 non-null      int64
#  1   실린더압력   3 non-null      float64
#  2   주조압력    3 non-null      float64
#  3   사이클타임   3 non-null      float64
#  4   비스킷두께   3 non-null      float64
#  5   형체력     3 non-null      float64
#  6   품질등급    3 non-null      str
# dtypes: float64(5), int64(1), str(1)
# memory usage: 300.0 bytes
#    샷  실린더압력    주조압력  사이클타임  비스킷두께형체력 품질등급
# 0  1  214.0  1037.0   20.7   10.0  258.0   양품
# 1  2  217.0  1052.0   20.7   11.0  257.0   양품
# 2  3  215.0  1040.0   20.7   21.0  253.0   주의

# 행(row)과 열(column) 언급 서브 DF 만들기
df_sub2 = df.loc[0:2, ["품질등급", "형체력"]]
df_sub2.info()
# <class 'pandas.DataFrame'>
# RangeIndex: 3 entries, 0 to 2
# Data columns (total 2 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   품질등급    3 non-null      str
#  1   형체력     3 non-null      float64
# dtypes: float64(1), str(1)
# memory usage: 180.0 bytes

print(df_sub2)
# 품질등급    형체력
# 0   양품  258.0
# 1   양품  257.0
# 2   주의  253.0
