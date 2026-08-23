import pandas as pd

df = pd.read_csv("data/15_02_사출성형_공정.csv", encoding="utf-8")

# 실습 5. fillna 평균·중앙값 대체
# 결측을 평균과 중앙값으로 채우고 차이 이해
print(df["최대사출압"].isna().sum())  # 60개 NaN 확인

print("=" * 40)
# · 대상 컬럼의 평균과 중앙값을 각각 구해 비교
# · fillna로 평균을 채운 결과 만들기
mean_value = df["최대사출압"].mean()
print(f"최대사출압의 평균 : {mean_value}")
# 최대사출압의 평균 : 1241.6723684210526

print("=" * 40)
s_fillmean = df["최대사출압"].fillna(mean_value)
print(s_fillmean)
# 0      1241.672368
# 1      1241.672368
# 2      1235.220000
# 3      1240.090000
# 4      1241.672368
#           ...
# 245    1237.590000
# 246    1238.090000
# 247    1241.672368
# 248    1241.672368
# 249    1232.610000
# Name: 최대사출압, Length: 250, dtype: float64

print("=" * 40)
df["최대사출압"] = s_fillmean
print(df["최대사출압"].isna().sum())
# 최대사출압 컬럼의 NaN 0개

print("=" * 40)
# · fillna로 중앙값을 채운 결과 만들기(이상치에 강함)
median_value = df["최대사출압"].median()
print(f"최대사출압의 중앙값 : {median_value}")
# 최대사출압의 중앙값 : 1240.84

print("=" * 40)
s_fillmedian = df["최대사출압"].fillna(median_value)
print(s_fillmedian)
# 0      1241.672368
# 1      1241.672368
# 2      1235.220000
# 3      1240.090000
# 4      1241.672368
#           ...
# 245    1237.590000
# 246    1238.090000
# 247    1241.672368
# 248    1241.672368
# 249    1232.610000
# Name: 최대사출압, Length: 250, dtype: float64

print("=" * 40)
df["최대사출압"] = s_fillmedian
print(df["최대사출압"].isna().sum())
# 최대사출압 컬럼의 NaN 0개

# 예상 결과
# 센서17 평균 466.26·중앙값 465.9로 대체, 남은 결측 0
