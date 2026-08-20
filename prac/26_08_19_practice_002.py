import pandas as pd

df = pd.read_csv("data/14_hydraulic_qc.csv", encoding="utf-8")

# 실습 2. 그룹별 통계 응용
# qc 합격·불합격 그룹별 지표 통계 비교
# 합격·불합격 그룹의 지표 평균과 표준편차 비교 -> 검사결과로 그룹만들기 groupby

# · 판정 열로 그룹을 나눠 주요 지표들의 평균 집계 -> mean
feats = ["지표02", "지표04"]
print(df.groupby("검사결과")[feats].mean().round(2))
#       지표02   지표04
# 검사결과
# 불합격   0.72  19.65
# 합격    0.55  46.88

# · 같은 그룹 기준으로 표준편차를 구해 흩어짐 비교 -> std
print(df.groupby("검사결과")[feats].std().round(2))
#       지표02  지표04
# 검사결과
# 불합격   0.05  0.70
# 합격    0.01  0.91

# · 두 그룹의 통계 차이를 읽어 불량의 특징 관찰
# 지표1과 지표5 모두 합격이 불합격보다 표준편차가 훨씬 작다
