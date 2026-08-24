import pandas as pd

df = pd.read_csv("data/16_diecasting.csv", encoding="utf-8")
print(df.head(3))

# 사이클타임 컬럼의 IQR 활용
q1 = df["사이클타임"].quantile(0.25)
q3 = df["사이클타임"].quantile(0.75)
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

# 상한선과 하한선을 이용해서 필터링할 조건을 만들 수 있다.
# 상한선~하한선 안쪽 : 정상범위로 판단
# 상한선과 하한선 바깥 : 이상하다고 판단 -> mask
mask = (df["사이클타임"] < lower) | (df["사이클타임"] > upper)
print(mask.sum())  # 6개는 정상범위 밖 확인
print(df[mask].shape)  # (6, 7) : 6개 이상한 것들의 df
print(df[~mask].shape)  # (196, 7) : ~은 NOT이라는 여집합을 의미 -> 정상범위

# 정상범위는 다음의 마스크를 사용해도 됨
mask_ok = (df["사이클타임"] >= lower) & (df["사이클타임"] <= upper)
print(df[mask_ok].shape)  # (182, 7) : 이 경우는 결측치는 제외함

df_clean = df[~mask]  # 이상한걸 제외한 나머지 멀쩡한 결과들 : 이상치 제거하기
print(len(df), len(df_clean))  # 202 196 -> 6개의 이상치 제거 확인
print(df_clean["사이클타임"].mean())  # 이상치가 제거된 값들의 평균 27.275824175824173

# 경계값으로 보정하기
# clip(lower, upper) 보정: 하한보다 작으면 하한값으로, 상한보다 크면 상한값으로 강제 평탄화
# (Windsorizing)합니다. 시계열 신호나 추세가 깨지지 않고 데이터 수도 그대로 유지되는 현업 다빈도 기법
df["사이클타임_clipped"] = df["사이클타임"].clip(lower=lower, upper=upper)
print(df["사이클타임_clipped"].agg(["min", "max", "mean"]))
# min     20.600000
# max     58.612500
# mean    28.275931
# Name: 사이클타임_clipped, dtype: float64

# 결측치로 바꿔 채우기
# ~mask(조건) + fillna(중앙값) : 이상치를 일단 빈칸(NaN)으로 강제 변환한 뒤, 중앙값으로
# 부드럽게 채워 넣어 수치 왜곡을 차단합니다.
s_masked = df["사이클타임"].mask(mask)
s_masked.info()
# <class 'pandas.Series'>
# RangeIndex: 202 entries, 0 to 201
# Series name: 사이클타임
# Non-Null Count  Dtype
# --------------  -----
# 182 non-null    float64
# dtypes: float64(1)
# memory usage: 1.7 KB
print(s_masked.head())
# 0    20.7
# 1    20.7
# 2    20.8
# 3    20.6
# 4    20.6
# Name: 사이클타임, dtype: float64

print(s_masked.isna().sum())  # 20

s_fixed = s_masked.fillna(s_masked.median())
s_fixed.info()
# <class 'pandas.Series'>
# RangeIndex: 202 entries, 0 to 201
# Series name: 사이클타임
# Non-Null Count  Dtype
# --------------  -----
# 202 non-null    float64
# dtypes: float64(1)
# memory usage: 1.7 KB
print(s_fixed.mean())  # 26.802970297029702

print(s_fixed.isna().sum())  # 0
