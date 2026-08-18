# 실습6. 필터링과 정렬 연결
# 조건으로 거른 결과에 정렬을 이어 붙이기
import pandas as pd

df = pd.read_csv("data/13_diecasting_shot.csv")
df.info()

# · 고장 여부 조건으로 고장 설비만 먼저 거르기
# "품질등급" 컬럼 == "불량"
df_filtered = df[df["품질등급"].isin(["불량"])]

# · 거른 결과에 sort_values를 점으로 이어 비스킷두께 내림차순 정렬
df_sorted_after_filtered = df[df["품질등급"].isin(["불량"])].sort_values(
    "비스킷두께", ascending=False
)

# · head로 상위 다섯 개만 남겨 샷 확인
print(df_sorted_after_filtered.head(5))
#        샷  실린더압력   주조압력  사이클타임  비스킷두께    형체력 품질등급
# 197  198  113.0  255.0   36.6   27.0  354.0   불량
# 191  192  113.0  255.0   36.9   26.0  366.0   불량
# 196  197  265.0  595.0   36.2   20.0  355.0   불량
# 193  194  113.0  255.0   34.4   19.0  370.0   불량
# 198  199  264.0  595.0   36.1   19.0  372.0   불량

# 실습6 완.
