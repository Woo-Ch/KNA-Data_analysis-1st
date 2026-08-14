# 실습1. 단일 조건으로 행 추출하기
# 조건을 만들고 그 조건으로 원하는 행만 추출
import pandas as pd

df = pd.read_csv("data/13_diecasting_small.csv")
df.info()
# <class 'pandas.DataFrame'>
# RangeIndex: 30 entries, 0 to 29
# Data columns (total 7 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   샷       30 non-null     int64
#  1   실린더압력   30 non-null     float64
#  2   주조압력    30 non-null     float64
#  3   사이클타임   30 non-null     float64
#  4   비스킷두께   30 non-null     float64
#  5   형체력     30 non-null     float64
#  6   품질등급    30 non-null     str
# dtypes: float64(5), int64(1), str(1)
# memory usage: 1.8 KB


# 비교 연산자로 실린더압력 기준의 조건식을 만들어 Boolean Series 생성
s = df["실린더압력"]
s.info()
s_boolean = s >= 230
s_boolean.info()  # dtypes: bool

# sum으로 조건을 만족하는 행 개수 확인
print(s_boolean.sum())  # 5

# 만든 조건을 데이터프레임 대괄호에 넣어 행 추출 -> 행의 갯수 출력
# 전체 df를 대상으로 앞서 특정 컬럼에 대한 불리언 시리즈를
# 컬럼 요구하는 [] 사이에 넣어주면,
# 각 줄마다 비교를 해서 True인 경우만 추려 새로운 df를 만든다.
df_sub = df[df["실린더압력"] >= 230]
df_sub.info()
# <class 'pandas.DataFrame'>
# RangeIndex: 5 entries, 7 to 27
# Data columns (total 7 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   샷       5 non-null      int64
#  1   실린더압력   5 non-null      float64
#  2   주조압력    5 non-null      float64
#  3   사이클타임   5 non-null      float64
#  4   비스킷두께   5 non-null      float64
#  5   형체력     5 non-null      float64
#  6   품질등급    5 non-null      str
# dtypes: float64(5), int64(1), str(1)
# memory usage: 412.0 bytes


# 예상 결과
# 참 개수와 추출 행 수가 같게 출력 (실린더압력 230 이상 5건)
print(len(df_sub))  # 5
