import pandas as pd

# 1단계. 원본 데이터 불러오기
log_before = pd.read_csv("data/15_사출성형_로그.csv", encoding="utf-8")


# 조건 필터링으로 위장 결측값 확인
print((log_before["배럴온도"] == 999).sum())
print((log_before["스크루속도"] == -999).sum())


# 변환 전 전체 결측값 개수 확인
before_count = log_before.isna().sum().sum()

print("변환 전 결측:", before_count)

log_after = pd.read_csv(
    "data/15_사출성형_로그.csv", encoding="utf-8", na_values=[-999, 999]
)

# 실습 3. 위장 결측 사냥
# 조건과 na_values로 위장 결측을 진짜 결측으로 전환
# 위장 결측을 조건과 na_values로 진짜 결측으로 전환

# · 위장 결측이 있는 열을 조건 필터링으로 추출해 확인
print((log_after["배럴온도"] == 999.0).sum())  # 1 -> 0
print((log_after["스크루속도"] == -999.0).sum())  # 2 -> 0


after_count = log_after.isna().sum().sum()

print("변환 후 결측:", after_count)
