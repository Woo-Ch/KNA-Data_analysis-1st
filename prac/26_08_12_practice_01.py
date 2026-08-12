# 실습1. CSV 불러오기 워밍업

import pandas as pd
import os

filepath = os.path.join("data", "12_metro_small.csv")
df = pd.read_csv(filepath)

print(df.shape)  # (30, 7)

print(df.head(1))  # head를 무작정 쓰기보단 뒤에()를 사용하여 몇개 불러올지 지정
# 측정시각  압축압력  배출압력  저장압력  오일온도  모터전류 가동상태
# 0  2020-02-27 06:38:47   9.3 -0.02   9.3  51.3  6.04   가동


# 파일을 못 찾을 경우를 대비하여 코드 작성
filepath = os.path.join("data", "12_metro_small.csv")

try:
    df = pd.read_csv(
        filepath,
        encoding="utf-8",
        sep=",",
        index_col="측정시각",
        nrows=5,
        usecols=["측정시각", "가동상태"],
    )
    # 파일 읽기 오류시 인코딩해볼 것. encoding="utf-8"

    print(df.shape)

    print(df.head(1))
except FileNotFoundError:
    print(f"파일이 없습니다: {filepath}")
