import pandas as pd

df = pd.read_csv("data/16_diecasting.csv")

# 실습6. 처리전 후 통계비교
# 제거·보정·중앙값 채움 세 처리의 평균 변화 비교

# 목표
# 제거·보정·중앙값 채움 세 처리의 평균 변화 비교

# 단계
# · 실린더압력 이상치 경계와 조건을 만들기
Q1 = df["실린더압력"].quantile(0.25)
Q3 = df["실린더압력"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

mask = (df["실린더압력"] < lower) | (df["실린더압력"] > upper)
fill = df["실린더압력"].mask(mask).fillna(df["실린더압력"].mask(mask).median())

# · 제거·보정·중앙값 채움 세 방식을 각각 적용

# · 처리 전 평균과 세 방식의 평균을 나란히 비교
print(round(df["실린더압력"].mean(), 2))  # 234.31  # 전
print(round(df[~mask]["실린더압력"].mean(), 2))  # 238.39  # 제거
print(round(df["실린더압력"].clip(lower, upper).mean(), 2))  # 235.31  # 보정
print(round(fill.mean(), 2))  # 238.05  # 채움

# 예상 결과
# 전 234.31 → 제거 238.39·보정 235.31·채움 238.05
