# 실습3. 공정 센서 열 골라내기

import pandas as pd

df = pd.read_csv("data/13_diecasting_shot.csv")

# 한 센서 열을 Series로 선택
# "형체력" 선택
df["형체력"].info()  # <class 'pandas.Series'>

# 여러 feature 열을 DataFrame으로 선택해 형태 확인
# df[["형체력", "실린더압력", "주조압력"]].shape 출력
print(df[["형체력", "실린더압력", "주조압력"]].shape)  # (200, 3)
