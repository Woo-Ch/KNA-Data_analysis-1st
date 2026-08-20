# 실습 5. 그룹별 평균 비교와 정렬
# 그룹별 평균을 구해 정렬로 두드러진 그룹 찾기
# 그룹별 평균을 구하고 정렬해 두드러진 그룹 찾기
import pandas as pd

df = pd.read_csv("data/14_hydraulic.csv", encoding="utf-8")
df.info()
# 0   냉각기상태   120 non-null    str
#  1   운전부하    120 non-null    str
#  2   밸브상태    120 non-null    str
#  3   온도      120 non-null    float64
#  4   진동      120 non-null    float64
#  5   압력      120 non-null    float64
#  6   냉각효율    120 non-null    float64
#  7   result  120 non-null    str

# · 설비로 그룹을 나눠 진동 평균 집계
# 냉각기상태 그룹별로 진동의 평균
print(df.groupby("냉각기상태")["진동"].mean().round(3))
# 냉각기상태
# 고장    0.688
# 저하    0.610
# 정상    0.549

# · 집계 결과에 정렬을 이어 붙여 오름차순으로 정렬
# 앞선 평균결과에 맞춰서 정상 > 저하 > 고장 순서로 출력
print(df.groupby("냉각기상태")["진동"].mean().round(3).sort_values(ascending=True))
# 냉각기상태
# 정상    0.549
# 저하    0.610
# 고장    0.688

# · 가장 진동이 큰 설비를 맨 위에서 확인
# 앞선 결과에서 심각 0.629가 맨 윗줄인걸 확인. 끝.
