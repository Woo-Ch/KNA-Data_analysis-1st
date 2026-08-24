import pandas as pd

df = pd.read_csv("data/16_diecasting.csv")

# 실습9. reset_index로 인덱스 정리
# 중복 제거로 생긴 인덱스 구멍을 다시 매기기

# 목표
# 중복 제거로 생긴 인덱스 구멍을 0부터 다시 매기기

print(len(df))  # 202

# 단계
# · drop_duplicates로 중복을 제거
delete_df = df.drop_duplicates()
print(len(delete_df))  # 200

# · reset_index로 인덱스를 0부터 다시 매기기
delete_df_reset = delete_df.reset_index(drop=True)
# delete_df의 인덱스를 0부터 다시 정리하고 기존 인덱스는 버린 뒤 저장
print(len(delete_df_reset))  # 200

# · 인덱스 최솟값·최댓값으로 연속성 확인
print(delete_df_reset.index.min())  # 0
print(delete_df_reset.index.max())  # 199

# 예상 결과
# 인덱스 0~199로 연속, 최종 200행
