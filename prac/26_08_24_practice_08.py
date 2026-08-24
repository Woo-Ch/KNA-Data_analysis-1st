import pandas as pd

df = pd.read_csv("data/16_diecasting.csv")

# 실습8. drop_duplicates로 중복제거
# 완전 중복 제거와 기준 컬럼 제거를 비교

# 목표
# 완전 중복 제거와 기준 컬럼 지정 제거를 비교

print(len(df))  # 202

# 단계
# · drop_duplicates로 완전 중복 행 제거
delete_df = df.drop_duplicates()

# · 제거 후 행 수와 남은 중복 개수 확인
print(len(delete_df))  # 200

# · subset으로 특정 컬럼만 기준 삼아 제거
delete_df_shot = df.drop_duplicates(subset=["샷"], keep="last")
print(len(delete_df_shot))  # 200

# 예상 결과
# 202행 → 200행, 남은 중복 0, subset 기준도 200행
