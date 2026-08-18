# 실습 7. 이상 의심 설비 리포트
# 불러오기부터 판단 문장까지 전체 워크플로우를 두 데이터에 적용
import pandas as pd

# 분석 워크플로우 5단계 맞춰가기
# 1. 불러오기
df = pd.read_csv("data/13_diecasting_shot.csv", encoding="utf-8")

# 2. 확인하기
df.info()
# <class 'pandas.DataFrame'>
# RangeIndex: 200 entries, 0 to 199
# Data columns (total 7 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   샷       200 non-null    int64
#  1   실린더압력   186 non-null    float64
#  2   주조압력    186 non-null    float64
#  3   사이클타임   186 non-null    float64
#  4   비스킷두께   186 non-null    float64
#  5   형체력     186 non-null    float64
#  6   품질등급    200 non-null    str
# dtypes: float64(5), int64(1), str(1)
# memory usage: 11.1 KB

# 3. 필터링
not_ok = df[(df["비스킷두께"] >= 20) | (df["사이클타임"] >= 50)]
print(len(not_ok))  # 11

# 4. 정렬
report = not_ok.sort_values("비스킷두께", ascending=False)
print(report.head())
#  샷  실린더압력    주조압력  사이클타임  비스킷두께    형체력 품질등급
# 197  198  113.0   255.0   36.6   27.0  354.0   불량
# 191  192  113.0   255.0   36.9   26.0  366.0   불량
# 42    43  215.0  1040.0   20.7   21.0  253.0   주의
# 196  197  265.0   595.0   36.2   20.0  355.0   불량
# 170  171  265.0   596.0   36.1   20.0  370.0   주의

# 5. 선택 : [[...]] 대괄호 중첩 주의!!
df_final = report[["샷", "품질등급", "형체력", "사이클타임"]]

print("-------------------")
print("가장 위험 목록")
print(df_final.head())
#  샷 품질등급    형체력  사이클타임
# 197  198   불량  354.0   36.6
# 191  192   불량  366.0   36.9
# 42    43   주의  253.0   20.7
# 196  197   불량  355.0   36.2
# 170  171   주의  370.0   36.1

df_danger = df_final.head(1)
print("가장 위험한 항목")
print(df_danger)
# 샷 품질등급    형체력  사이클타임
# 197  198   불량  354.0   36.6

print("=======================선택 ==========================")
# · 복합 조건으로 위험 설비를 거르고 비스킷두께 내림차순 정렬
# · 필요한 주요 열만 선택하고 가장 위험한 설비로 판단 문장 작성
# · 같은 흐름을 주조 로그 불량 데이터에도 적용해 결과 비교

# 예상 결과
# 주조 로그 위험 50건·판단 문장, 주조 로그 불량 상위 목록 출력

danger = df[(df["비스킷두께"] >= 20) | (df["사이클타임"] >= 50)]

print("주조 로그 위험 건수:", len(danger))


# 비스킷두께가 큰 순서로 정렬
danger_sorted = danger.sort_values("비스킷두께", ascending=False)


# 필요한 주요 열만 선택
danger_report = danger_sorted[["샷", "품질등급", "비스킷두께", "형체력", "사이클타임"]]

print("\n주조 로그 위험 상위 목록")
print(danger_report.head())


# 가장 위험한 항목 1개 선택
most_danger = danger_report.head(1)

shot = int(most_danger["샷"].tolist()[0])
biscuit = most_danger["비스킷두께"].tolist()[0]
grade = most_danger["품질등급"].tolist()[0]

print(
    f"\n가장 위험한 샷은 {shot}번이며, "
    f"비스킷두께는 {biscuit}, 품질등급은 {grade}입니다. "
    f"우선 점검이 필요합니다."
)


# 품질등급이 불량인 데이터만 추출
bad = df[df["품질등급"] == "불량"]


# 불량 데이터도 비스킷두께 내림차순 정렬
bad_sorted = bad.sort_values("비스킷두께", ascending=False)


# 필요한 열만 선택
bad_report = bad_sorted[["샷", "품질등급", "비스킷두께", "형체력", "사이클타임"]]

print("\n주조 로그 불량 상위 목록")
print(bad_report.head())
