# 실습1. 데이터 불러오기와 구조 확인하기

import pandas as pd

df = pd.read_csv("data/13_diecasting_small.csv")

# shape 확인
# columns의 열 이름 출력 확인
# 실제 CSV파일 열어보고 shape, columns 그대로 나온건지 비교

print(df.shape)  # (30, 7)

print(df.columns)
# Index(['샷', '실린더압력', '주조압력', '사이클타임', '비스킷두께', '형체력', '품질등급'], dtype='str')
