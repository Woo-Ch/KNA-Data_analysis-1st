import pandas as pd

df = pd.read_csv("data/16_welding.csv")

# 실습10. 다른현장(용접) 이상치·중복 종합 정제
# 탐색→보정→중복 점검→저장을 다른 현장에 그대로

# 목표
# IQR 탐색부터 정제 데이터 저장까지 한 흐름으로

# 단계
# · 용접 통전전류의 IQR 경계로 이상치 개수·비율 확인
c = "통전전류"

q1, q3 = df[c].quantile(0.25), df[c].quantile(0.75)
lower, upper = q1 - 1.5 * (q3 - q1), q3 + 1.5 * (q3 - q1)
m = (df[c] < lower) | (df[c] > upper)
print(int(m.sum()), round(m.mean() * 100, 1))  # 24  14.8

# · clip으로 이상치를 보정하고 중복을 제거·정리
print(len(df))  # 162
df[c] = df[c].clip(lower=lower, upper=upper)
df = df.drop_duplicates().reset_index(drop=True)
print(len(df))  # 158

# · 정제한 데이터를 파일로 저장
df.to_csv("data/16_welding.csv", index=False)

# 예상 결과
# 용접 통전전류 이상치 24건(14.8%), 보정·중복 제거 후 저장
