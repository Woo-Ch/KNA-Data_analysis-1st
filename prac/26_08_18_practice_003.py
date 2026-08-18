# 실습3. 구간으로묶어세기
# pd.cut으로 수치형 값을 구간으로 묶어 빈도 세기
# 목표
# 수치형 센서 값을 구간으로 나눠 분포 확인
import pandas as pd

df = pd.read_csv("data/14_hydraulic.csv", encoding="utf-8")
df.info()

# 단계
# · 진동 열의 최솟값과 최댓값으로 값의 범위 확인
print(df["진동"].min())  # 0.53
print(df["진동"].max())  # 0.779

# · pd.cut으로 경계와 이름표를 정해 세 구간으로 묶기
band = pd.cut(df["진동"], bins=[0.0, 0.6, 0.7, 1.0], labels=["약함", "보통", "강함"])

# · 묶은 구간에 value_counts로 구간별 빈도 세기
print(band.value_counts())
# 진동
# 보통    55
# 약함    48
# 강함    17
