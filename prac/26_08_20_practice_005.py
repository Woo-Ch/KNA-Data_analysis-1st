import pandas as pd

df = pd.read_csv("data/15_01_사출성형_공정.csv", encoding="utf-8")

# 실습 5. 결측 순위와 행별 분석
# 정렬과 행 방향 카운트로 컬럼·행 두 방향 확인
# 컬럼 순위와 행별 결측을 함께 봐 처리 근거 모으기

counts = df.isna().sum()

data_ratio = (counts / len(df) * 100).round(1)

# · 결측 비율을 내림차순 정렬해 가장 심한 컬럼 확인
print(data_ratio.sort_values(ascending=False).head(3))
# 감압시간     43.6
# 계량종료점    43.6
# 최소쿠션     27.2

# · 방향을 가로(행)로 바꿔 행마다 결측 개수 세기
# NaN 합산대상을 Y축방향별로 컬럼별로 하는게 아니라
# X축방향별로 각 row마다 처리하기
df_axis = df.isna().sum(axis=1)
print(f"결측없는 행 {(df_axis == 0).sum()}개")  # 결측없는 행 76개
print(f"결측있는 행 {(df_axis > 0).sum()}개")  # 결측있는 행 174개

# · 결측이 많은 부실 행만 조건으로 골라내기
print(f"결측 5개 이상있는 행 {(df_axis >= 5).sum()}개")  # 결측 5개 이상있는 행 27개

# 예상 결과
# 센서19·20 최상위, 결측 없는 행 76·있는 행 174
