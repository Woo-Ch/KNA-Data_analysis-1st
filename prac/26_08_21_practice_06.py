import pandas as pd

df = pd.read_csv("data/15_02_사출성형_공정.csv", encoding="utf-8")

# 실습 6. 최빈값·앞뒤 값 대체
# 범주형은 최빈값, 시계열은 앞뒤 값으로 채우기

# · 범주형 열의 최빈값을 구해 채우기
# 사출기 컬럼은 1혹기~3호기 범주형으로 판단
print(df["사출기"].isna().sum())  # 억지로 3개 만들어봤어요!
# 0
print(df["사출기"].mode()[0])  # 1호기가 가장 많다고 함
# 1호기

df["사출기"] = df["사출기"].fillna(df["사출기"].mode()[0])
print(df["사출기"].isna().sum())  # 다시 채워서 0개!
# 0

# · 측정시각 순으로 정렬해 시계열 순서 만들기
df = df.sort_values("측정시각")

# · ffill로 앞 값, bfill로 남은 앞쪽 결측까지 채우기
print(df["전환압력"].isna().sum())
# 68개 NaN 확인
df["전환압력"] = df["전환압력"].ffill().bfill()  # 자주 볼 시계열 채우기 패턴
print(df["전환압력"].isna().sum())
# 0개 NaN 확인
# ffill과 bfill으로 다 채웠기 때문에 0개로 나옴

# 결과
# 사출기는 최빈값(1호기)으로 결측값 대체
# 전환압력은 측정시각 순으로 정렬한 뒤 앞뒤 값(ffill, bfill)으로 결측값 대체
# 대체 후 사출기와 전환압력의 결측값은 0개
