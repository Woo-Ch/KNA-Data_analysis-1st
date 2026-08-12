# 실습 4. 필요한 열만 골라 불러오기
# G O A L usecols와 nrows로 열 많은 데이터에서 필요한 부분만

# 센서 3개만 골라 불러오기
# usecols=[...]

# usecols로 필요한 열만 읽어 shape 변화 확인
# 열이 7개— usecols로 4열만 고르면 200행 4열로 축소

import pandas as pd

df = pd.read_csv("data/12_metro_compressor.csv", usecols=["측정시각", "오일온도"])
print(df.shape)  # (200, 7)
print(df.head(3))
# 측정시각  오일온도
# 0  2020-02-27 06:38:47  51.3
# 1  2020-02-27 07:28:21  56.8
# 2  2020-02-27 08:17:54  55.7
