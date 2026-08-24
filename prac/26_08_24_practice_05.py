import pandas as pd

df = pd.read_csv("data/16_diecasting.csv")

# 실습5. 경계값 보정 clipping
# 이상치를 버리지 않고 경계값으로 눌러 보정

# 목표
# 이상치를 버리지 않고 경계값으로 눌러 보정

Q1 = df["사이클타임"].quantile(0.25)
Q3 = df["사이클타임"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR

upper = Q3 + 1.5 * IQR

mask = (df["사이클타임"] < lower) | (df["사이클타임"] > upper)

# 단계
# · clip으로 하한보다 작은 값은 하한으로 올리기
stat_fix = df["사이클타임"].clip(lower=lower, upper=upper)

# · 상한보다 큰 값은 상한으로 내리기

# · 보정 후 최솟값·최댓값·평균 확인
print(round(stat_fix.min(), 2), round(stat_fix.max(), 2))  # 20.6  58.61
print(round(stat_fix.mean(), 2))  # 28.28

# 예상 결과
# 보정 후 최소 20.6·최대 58.6, 평균 28.28
