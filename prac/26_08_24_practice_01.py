import pandas as pd

df = pd.read_csv("data/16_diecasting.csv")

# 실습1. IQR과 이상치 경계 구하기
# 사이클타임의 IQR과 1.5배 규칙 하한·상한 계산

# 목표
# IQR과 1.5배 규칙으로 이상치 경계를 구하기

# 단계
# · 사이클타임의 25%·75% 값을 구해 IQR(Q3-Q1) 계산
Q1 = df["사이클타임"].quantile(0.25)
Q3 = df["사이클타임"].quantile(0.75)
IQR = Q3 - Q1

print(Q1, Q3, IQR)
# 20.8 35.925 15.124999999999996

# · Q1에서 IQR의 1.5배를 빼 하한 계산
lower = Q1 - 1.5 * IQR

# · Q3에 IQR의 1.5배를 더해 상한 계산
upper = Q3 + 1.5 * IQR

# 예상 결과
print(round(IQR, 2))  # 15.12
print(round(lower, 1))  # -1.9
print(round(upper, 1))  # 58.6

# 사이클타임 IQR 15.12, 하한 -1.9·상한 58.6
