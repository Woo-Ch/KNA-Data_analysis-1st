import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", 1000)


# ==========================================
# STEP 0. 데이터 불러오기
# ==========================================

tags = pd.read_csv("Allie/03-01_회전기계_신호_회전기계태그목록.csv")

df = pd.read_csv("Allie/03-01_회전기계_신호_진동추세.csv")


# ==========================================
# STEP 1. 보유 태그 확인
# ==========================================

MTR = tags[tags["tag"].str.startswith("MTR01")]

FAN = tags[tags["tag"].str.startswith("FAN01")]

print("========== 1번 모터 ==========")
print(MTR.to_string(index=False))

print("\n========== 1번 팬 ==========")
print(FAN.to_string(index=False))


# ==========================================
# STEP 2. CASE A - 베어링 손상
# ==========================================

case_a = {
    "베어링 가속도 진동": "MTR01_VIB_ACC",
    "수평 진동": "MTR01_VIB_H",
    "모터 온도": "MTR01_TEMP",
    "모터 회전수": "MTR01_RPM",
    "모터 전류": "MTR01_CURRENT",
}

print("\n========== CASE A ==========")

for name, tag in case_a.items():

    if tag in df.columns:
        print(f"{name} | O | {tag}")
    else:
        print(f"{name} | X | 없음")


# ==========================================
# STEP 3. CASE B - 팬 불평형
# ==========================================

case_b = {
    "팬 수평 진동": "FAN01_VIB_H",
    "팬 수직 진동": "FAN01_VIB_V",
    "팬 가속도 진동": "FAN01_VIB_ACC",
    "팬 회전수": "FAN01_RPM",
    "팬 전류": "FAN01_CURRENT",
}

print("\n========== CASE B ==========")

for name, tag in case_b.items():

    if tag in df.columns:
        print(f"{name} | O | {tag}")
    else:
        print(f"{name} | X | 없음")


# ==========================================
# STEP 4. 실제 사용 가능한 분석 컬럼
# ==========================================

cols = list(case_a.values()) + list(case_b.values())

# 중복 제거 + 실제 존재 컬럼만 선택
cols = list(dict.fromkeys(cols))
cols = [c for c in cols if c in df.columns]


# ==========================================
# STEP 5. min / max / mean
# ==========================================

print("\n========== 기초 통계 ==========")

print(df[cols].agg(["min", "max", "mean"]).round(2).to_string())


# ==========================================
# STEP 6. 값이 변한 최소 폭
# ==========================================

print("\n========== 값이 변한 최소 폭 ==========")

for col in cols:

    values = sorted(df[col].dropna().unique())

    min_change = pd.Series(values).diff().dropna().min()

    print(f"{col} : {min_change}")
