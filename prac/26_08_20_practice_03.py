import pandas as pd

df_qc = pd.read_csv("data/14_hydraulic_qc.csv", encoding="utf-8")
df_qc.info()
# <class 'pandas.DataFrame'>
# RangeIndex: 200 entries, 0 to 199
# Data columns (total 11 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   검사결과    200 non-null    str
#  1   지표01    200 non-null    float64
#  2   지표02    200 non-null    float64
#  3   지표03    200 non-null    float64
#  4   지표04    200 non-null    float64
#  5   지표05    200 non-null    float64
#  6   지표06    200 non-null    float64
#  7   지표07    200 non-null    float64
#  8   지표08    200 non-null    float64
#  9   지표09    200 non-null    float64
#  10  지표10    200 non-null    float64
# dtypes: float64(10), str(1)
# memory usage: 17.3 KB

# 실습 3. 그룹별 상관 비교
# 같은 센서 쌍의 상관이 그룹에 따라 달라지는지 비교

# · 판정 열로 합격·불합격 그룹을 나누기 -> df_qc['검사결과']
# · 각 그룹에서 같은 두 지표의 상관계수를 계산
# -> 합격 그룹, 불합격 그룹별로 지표07과 지표08 상관관계?
# · 전체·합격·불합격 상관을 비교하고 표본 수 주의

# 전체 데이터의 지표07과 지표08 상관관계
r_all = df_qc["지표07"].corr(df_qc["지표08"])
print(r_all.round(3))  # -0.969

# 검사결과가 합격인 데이터 그룹의 지표07과 지표08 상관관계
df_qa = df_qc[df_qc["검사결과"] == "합격"]
r_qa = df_qa["지표07"].corr(df_qa["지표08"])
print(r_qa.round(3))  # 0.385

# 검사결과가 불합격인 데이터 그룹의 지표07과 지표08 상관관계
df_nqa = df_qc[df_qc["검사결과"] == "불합격"]
r_nqa = df_nqa["지표07"].corr(df_nqa["지표08"])
print(r_nqa.round(3))  # -0.998

# [해석]
# 검사결과 합격의 경우 지표07과 08사이에 관계성이 약함
# 불합격이라면 그 관계성이 강하다

# 예상 결과
# 전체 -0.969, 합격 0.482, 불합격 0.564 (불합격 12건 주의)

print("전체 데이터 수:", len(df_qc))  # 전체 데이터 수: 200
print("합격 데이터 수:", len(df_qa))  # 합격 데이터 수: 188
print("불합격 데이터 수:", len(df_nqa))  # 불합격 데이터 수: 12
