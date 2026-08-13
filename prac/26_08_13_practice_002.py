# 실습2. 열 선택하기

import pandas as pd

df = pd.read_csv("data/13_diecasting_small.csv")

# 대괄호 한 겹으로 단일 열을 Series로 선택
# "형체력" 컬럼 하나만 빼오기
df["형체력"].info()  # <class 'pandas.Series'>

# 대괄호 두 겹으로 복수 열을 DataFrame으로 선택
# "형체력", "실린더압력" 두 개를 선택하기
df[["형체력", "실린더압력"]].info()  # <class 'pandas.DataFrame'>


# 선택한 열에 mean으로 평균 계산
# df["형체력"].mean() - > round로 소수점 이하 1자리까지만 나오게 조정

print(round(df["형체력"].mean(), 1))  # 267.8
