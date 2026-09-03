import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)

tags = pd.read_csv("Allie/03-01_유압·열설비_신호_계통태그목록.csv")
df = pd.read_csv("Allie/03-01_유압·열설비_신호_유압운전.csv")

print("================STEP 1================")
# [Step 1] 주요 태그 확인

# HYD로 시작하는 태그를 확인하고 아래 항목을 정리하세요. (유압 계통)
# Python으로 진행해주세요.


print(
    tags.loc[
        tags["tag"].str.startswith("HYD"),
        ["tag", "physical_qty", "unit", "circuit_position"],
    ]
)
#              tag           physical_qty   unit      circuit_position
# 0      HYD01_PRESS_PUMP           압력    bar           펌프 토출부
# 1   HYD01_PRESS_FILT_IN           압력    bar            필터 전단
# 2  HYD01_PRESS_FILT_OUT           압력    bar            필터 후단
# 3       HYD01_DP_FILTER           차압    bar       필터 전후단 계산값
# 4            HYD01_FLOW           유량  L/min         펌프 토출 배관
# 5         HYD01_OILTEMP           온도   degC            탱크 내부
# 6           HYD01_LEVEL           유면      %           탱크 유면계
# 7    HYD01_PUMP_CURRENT           전류      A           펌프 제어반
# 8       HYD01_VALVE_CMD           개도      %      방향 제어 밸브 지령
# 9        HYD01_VALVE_FB           개도      %      방향 제어 밸브 실제

print("================STEP 2================")
# [Step 2] 정상 구간과 최근 구간 비교

# 아래 5개 컬럼을 사용하세요.

# - HYD01_PRESS_PUMP
# - HYD01_FLOW
# - HYD01_OILTEMP
# - HYD01_LEVEL
# - HYD01_PUMP_CURRENT

# Python으로 다음 값을 구하세요.

# 1. 첫 30일 평균
# 2. 마지막 10일 평균


cols = [
    "HYD01_PRESS_PUMP",
    "HYD01_FLOW",
    "HYD01_OILTEMP",
    "HYD01_LEVEL",
    "HYD01_PUMP_CURRENT",
]

df["date"] = pd.to_datetime(df["date"])

daily = df.groupby(df["date"].dt.date)[cols].mean()
first_30 = daily.head(30).mean()
last_10 = daily.tail(10).mean()

print("=== 정상 30일 평균 ===")
print(first_30)
# HYD01_PRESS_PUMP      152.30
# HYD01_FLOW            117.95
# HYD01_OILTEMP          42.35
# HYD01_LEVEL            88.00
# HYD01_PUMP_CURRENT     31.45

print("=== 최근 10일 평균 ===")
print(last_10)
# HYD01_PRESS_PUMP      149.50
# HYD01_FLOW            116.95
# HYD01_OILTEMP          48.35
# HYD01_LEVEL            88.00
# HYD01_PUMP_CURRENT     32.45

print("================STEP 3================")

# [Step 3] 필터 차압 확인

# 필터 전단 압력과 후단 압력을 이용해 차압을 계산하세요.
# (차압은 csv 컬럼으로 관리하고 있지 않아서 직접 계산해야합니다)
# Python으로 진행해주세요.

# 차압 = 필터 전단 압력 - 필터 후단 압력

# 아래 3개 구간의 시작 차압과 종료 차압을 비교하세요.

# 구간       | 시작 차압 | 종료 차압 | 증가폭
# ----------|----------|----------|-------
# 1~30일    |          |          |
# 31~60일   |          |          |
# 61~90일   |          |          |

# 1   HYD01_PRESS_FILT_IN           압력    bar            필터 전단
# 2  HYD01_PRESS_FILT_OUT           압력    bar            필터 후단

df["date"] = pd.to_datetime(df["date"])

df["cal_pressure"] = df["HYD01_PRESS_FILT_IN"] - df["HYD01_PRESS_FILT_OUT"]

# 1~30일
start_1 = df.loc[df["date"] == "2026-01-01", "cal_pressure"].iloc[0]
end_1 = df.loc[df["date"] == "2026-01-30", "cal_pressure"].iloc[0]

# 31~60일
start_2 = df.loc[df["date"] == "2026-01-31", "cal_pressure"].iloc[0]
end_2 = df.loc[df["date"] == "2026-03-01", "cal_pressure"].iloc[0]

# 61~90일
start_3 = df.loc[df["date"] == "2026-03-02", "cal_pressure"].iloc[0]
end_3 = df.loc[df["date"] == "2026-03-31", "cal_pressure"].iloc[0]

print("1~30일 :", start_1, end_1, end_1 - start_1)
print("31~60일:", start_2, end_2, end_2 - start_2)
print("61~90일:", start_3, end_3, end_3 - start_3)
# 1~30일 : 2.5 5.0 2.5
# 31~60일: 2.5 6.0 3.5
# 61~90일: 2.5 7.0 4.5

print("====================강사님 ver====================")


import pandas as pd

tags = pd.read_csv("Allie/03-01_유압·열설비_신호_계통태그목록.csv")
hyd = pd.read_csv("Allie/03-01_유압·열설비_신호_유압운전.csv")

# ===========
# Step 1.
# ===========
"""
HYD로 시작하는 태그를 확인
태그명 | 물리량 | 단위 | 회로 위치
"""
print(
    tags.loc[
        tags["tag"].str.startswith("HYD"),
        ["tag", "physical_qty", "unit", "circuit_position"],
    ]
)
"""
                    tag physical_qty   unit circuit_position
0      HYD01_PRESS_PUMP           압력    bar           펌프 토출부
1   HYD01_PRESS_FILT_IN           압력    bar            필터 전단
2  HYD01_PRESS_FILT_OUT           압력    bar            필터 후단
3       HYD01_DP_FILTER           차압    bar       필터 전후단 계산값
4            HYD01_FLOW           유량  L/min         펌프 토출 배관
5         HYD01_OILTEMP           온도   degC            탱크 내부
6           HYD01_LEVEL           유면      %           탱크 유면계
7    HYD01_PUMP_CURRENT           전류      A           펌프 제어반
8       HYD01_VALVE_CMD           개도      %      방향 제어 밸브 지령
9        HYD01_VALVE_FB           개도      %      방향 제어 밸브 실제
"""

# ===========
# Step 2.
# ===========
"""
- HYD01_PRESS_PUMP, HYD01_FLOW, HYD01_OILTEMP, 
- HYD01_LEVEL, HYD01_PUMP_CURRENT

유압 5개 컬럼에 대한 첫 30일 평균과 마지막 10일 평균
"""

COL = [
    "HYD01_PRESS_PUMP",
    "HYD01_FLOW",
    "HYD01_OILTEMP",
    "HYD01_LEVEL",
    "HYD01_PUMP_CURRENT",
]

# 첫 30일에 대한 평균값
print(hyd.head(30)[COL].agg(["mean", "min", "max"]).round(2))
"""
      HYD01_PRESS_PUMP  HYD01_FLOW  HYD01_OILTEMP  HYD01_LEVEL  HYD01_PUMP_CURRENT
mean             152.3      117.95          42.35         88.0               31.45
min              151.0      117.00          42.00         88.0               31.00
max              154.0      118.50          43.00         88.0               32.00
"""
# 최근 10일에 대한 평균값
print(hyd.tail(10)[COL].agg(["mean", "min", "max"]).round(2))
"""
      HYD01_PRESS_PUMP  HYD01_FLOW  HYD01_OILTEMP  HYD01_LEVEL  HYD01_PUMP_CURRENT
mean             149.5      116.95          48.35         88.0               32.45
min              148.0      116.00          47.50         88.0               32.00
max              151.0      117.50          49.50         88.0               33.00
"""

"""
펌프 압력 -> 감소
유량 -> 감소
유온 -> 증가
유면 -> 그대로
펌프 전류 -> 증가 
"""
# 내부 누설이나 펌프 동작에 문제가 있을 가능성이 있음.

# ===========
# Step 3.
# ===========
"""
구간별 필터 차압 구하기(전단 압력 - 후단 압력)
- 구간: 1~30일, 31~60일, 61~90일
- (구간별) 시작 차압, 종료차압, 증가폭
"""

# 차압: 필터 전단 압력 - 필터 후단 압력
hyd["DP"] = (hyd["HYD01_PRESS_FILT_IN"] - hyd["HYD01_PRESS_FILT_OUT"]).round(2)
# print(hyd["DP"].head())

for lo, hi in [(1, 30), (31, 60), (61, 90)]:
    # 30일과 60일에 필터를 교체했다고 가정
    seg = hyd.iloc[lo - 1 : hi]
    print(
        lo,
        hi,
        seg["DP"].iloc[0],  # 각 구간의 첫번째 날의 차압
        seg["DP"].iloc[-1],  # 각 구간의 마지막 날의 차압
        # 구간별 차압의 차(구간별로 차압이 얼마나 증가했는지)
        round(seg["DP"].iloc[-1] - seg["DP"].iloc[0], 2),
    )
    """
    1 30 2.5 5.0 2.5
    31 60 2.5 6.0 3.5
    61 90 2.5 7.0 4.5
     """
    # 차압이 증가하는 폭은 점점 커지고 있음
    # -> 필터 교체 이후 이전보다 빠르게 막히고 있다
    # -> 유체의 오염도가 시간이 흐름에 따라 증가하고 있음
