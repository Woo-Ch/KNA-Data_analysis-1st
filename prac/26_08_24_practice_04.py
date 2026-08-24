import pandas as pd

df = pd.read_csv("data/16_diecasting.csv")

# 실습4. 이상치 제거 후 크기 비교
# 경계 밖 행을 빼고 남은 크기와 평균 확인

# 목표
# 경계 밖 행을 제거하고 남은 크기·평균 확인

Q1 = df["사이클타임"].quantile(0.25)
Q3 = df["사이클타임"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR

upper = Q3 + 1.5 * IQR

mask = (df["사이클타임"] < lower) | (df["사이클타임"] > upper)

# 단계
# · 조건을 뒤집어 정상 범위 행만 남기기
stat_ok = df[~mask]

# · 원본과 제거 후의 행 수를 비교
print(len(df), len(stat_ok))  # 202 196

# · 제거 후 평균을 구해 변화 확인
print(round(df["사이클타임"].mean(), 2))  # 64.75
print(round(stat_ok["사이클타임"].mean(), 2))  # 27.28

# 예상 결과
# 202행 → 196행, 제거 후 사이클타임 평균 27.28
