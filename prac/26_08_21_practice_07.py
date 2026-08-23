import pandas as pd

df = pd.read_csv("data/15_02_사출성형_공정.csv", encoding="utf-8")

# 실습 7. 그룹별 대체
# 그룹별 평균으로 채워 집단 특성 반영

# · 제품유형으로 그룹을 나누기
print(df.groupby("사출기")["감압시간"].mean())
# 사출기별로 감압시간 평균이 다른 것 확인
# 1호기    0.322179
# 2호기    0.322368
# 3호기    0.322400

# · 각 그룹의 평균으로 그 그룹의 결측을 채우기

# 사출기별로 그룹을 나누고
# 그룹마다 갑압시간의 시리즈를 뽑아서
# 그 시리즈의 NaN들을 그 시리즈의 평균들로 채운다
df["감압시간"] = df.groupby("사출기")["감압시간"].transform(
    lambda s: s.fillna(s.mean())
)

print(df["감압시간"].isna().sum())  # 0

# · 남은 수치 결측은 전체 중앙값으로 마무리하고 검증
# 이런 코드는 실제로 할 가능성이 전혀 없음 - 컬럼의 특성고려 없이 NaN을 다 채운다?
df_numbers = df.select_dtypes("number")
df[df_numbers.columns] = df_numbers.fillna(df_numbers.median())
# 숫자만 인식한 뒤 Nan값을 중앙값으로 대체함

print(df.isna().sum())
# 측정시각      0
# 불량여부      0
# 사출기       0
# 사이클시간     0
# 성형사이클     0
# 배럴온도1     0
# 배럴온도2     0
# 배럴온도3     0
# 배럴온도4     0
# 호퍼온도      0
# 스크루속도     0
# 사출압력      0
# 스크루위치     0
# 전환위치      0
# 계량시간      0
# 계량시작위치    0
# 계량시작점     0
# 최소쿠션      0
# 최대사출압     0
# 전환압력      0
# 최대사출속도    0
# 감압시간      0
# dtype: int64

print(df.isna().sum().sum())
# 0

# 예상 결과
# 토크를 유형별 평균으로 대체, 남은 결측 0
