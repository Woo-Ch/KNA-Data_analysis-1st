import pandas as pd

df = pd.read_csv("data/16_diecasting.csv")

# 실습2. 한 컬럼의 최소·최대·범위

# 목표
# 한 컬럼의 최솟값·최댓값·범위를 구해 퍼짐 확인


# 단계
# · 실린더압력 열의 최소값 구하기
min_value = df["실린더압력"].min()
print(min_value)  # 108.0


# · 실린더압력 열의 최댓값 구하기
max_value = df["실린더압력"].max()
print(max_value)  # 265.0


# · 최댓값에서 최소값을 빼 범위 계산
range_value = max_value - min_value
print(range_value)  # 157.0


# 예상 결과
# 실린더압력 최소 108·최대 265·범위 157
