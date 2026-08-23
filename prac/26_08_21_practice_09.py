import pandas as pd

df = pd.read_csv("data/15_02_사출성형_공정.csv", encoding="utf-8")

# 실습 9. SECOM·AI4I 종합 처리
# 제거와 대체를 조합해 전체 결측을 처리하고 저장

# · 결측 비율 높은 컬럼을 제거하고 나머지는 중앙값으로 채우기
# 앞서 처리한 대체판 재사용!

기준 = df.drop(columns=["최대사출속도", "감압시간"])

제거판 = 기준.dropna()

대체판 = 기준.fillna(기준.median(numeric_only=True))

# · 처리 후 남은 결측과 크기를 확인하고 파일로 저장
print(대체판.isna().sum().sum())  # 0
대체판.to_csv("data/15_02_사출성형_공정_clean.csv", index=False, encoding="utf-8")

# · 같은 절차를 AI4I 데이터에도 반복해 결측 0 확인

# 예상 결과
# SECOM 결측 0·저장, AI4I 결측 0
