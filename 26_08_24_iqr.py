import pandas as pd

df = pd.read_csv("data/16_diecasting.csv", encoding="utf-8")
print(df.head(3))

# 실린더압력 컬럼의 IQR 활용
q1 = df["실린더압력"].quantile(0.25)
q3 = df["실린더압력"].quantile(0.75)
print(f"Q1: {q1}, Q3: {q3}")
# Q1: 215.75, Q3: 265.0
iqr = q3 - q1
print(f"IQR: {iqr}")
# IQR: 49.25

# 상한선과 하한선은 IQR의 1.5배를 적용한다
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
print(f"하한선: {lower}, 상한선: {upper}")
# 하한선: 141.875, 상한선: 338.875
