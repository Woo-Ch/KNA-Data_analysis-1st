import pandas as pd

df = pd.read_csv("data/15_02_사출성형_공정.csv", encoding="utf-8")

# 실습 4. 삭제 손실 비교
# 삭제 방식별 남는 행 수와 손실률을 표로 비교

# 단계
# · 원본·행삭제·thresh 각 방식의 남는 행 수 구하기
# · 방식과 행 수를 하나의 표로 모으기

# 1. 원본 행 수
original = len(df)
print("원본 행 수:", original)
# 250


# 2. 결측값이 하나라도 있는 행 모두 삭제
drop_all = len(df.dropna())
print("행삭제 후:", drop_all)
# 76


# 3. 값이 20개 이상 존재하는 행만 남기기
drop_thresh = len(df.dropna(thresh=20))
print("thresh=20 적용 후:", drop_thresh)
# 162


# 4. 행삭제 방식의 손실률
loss_all = (1 - drop_all / original) * 100
print("행삭제 손실률:", round(loss_all, 2))
# 69.6


# 5. thresh=20 방식의 손실률
loss_thresh = (1 - drop_thresh / original) * 100
print("thresh 손실률:", round(loss_thresh, 2))
# 35.2

# 위 코드는 너무 고급기술 - DF의 더 깊은 이해 경험 필요
# 여러분은 그냥 개별 3가지 항목들을 따로따로 계산시켜 출력해도 괜찮아요


# · 원본 대비 손실률을 백분율로 계산해 나란히 보기

# 예상 결과
# 행삭제 손실 약 70%, thresh 손실 약 35%
