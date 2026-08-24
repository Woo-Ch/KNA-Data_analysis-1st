import pandas as pd

df = pd.read_csv("data/16_diecasting.csv", encoding="utf-8")

# 실습5. quantile로 Q1·Q2·Q3
# 실린더압력의 사분위수를 구하고 Q2와 중앙값 일치 확인

# 목표
# 사분위수를 구하고 Q2가 중앙값과 같은지 확인

# 단계
# · 25% 지점 값을 quantile로 구해 Q1 확인
print(df["실린더압력"].quantile(0.25))  # 215.75

# · 50% 지점 값이 중앙값과 같은지 확인
print(df["실린더압력"].quantile(0.5))  # 218.0
print(df["실린더압력"].median())  # 218.0

# · 75% 지점 값을 구해 가운데 절반 범위 파악
print(df["실린더압력"].quantile(0.75))  # 265.0

# 예상 결과
# 실린더압력 Q1 215.75·Q2 218·Q3 265
