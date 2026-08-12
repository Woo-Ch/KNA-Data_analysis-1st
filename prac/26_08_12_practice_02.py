# 실습2. 설비 센서 CSV 불러오기
import pandas as pd

# 12_metro_compressor.csv
# 200행 7열- 인덱스 3번 행 오일온도가 NaN

df = pd.read_csv("data/12_metro_compressor.csv", encoding="utf-8")
print(df.head(3))
# 측정시각  압축압력  배출압력  저장압력  오일온도  모터전류 가동상태
# 0  2020-02-27 06:38:47  9.30 -0.02  9.30  51.3  6.04   가동
# 1  2020-02-27 07:28:21  8.55 -0.02  8.55  56.8  0.04   정지
# 2  2020-02-27 08:17:54  8.67 -0.02  8.67  55.7  0.03   정지
print(df.shape)  # (200, 7)
