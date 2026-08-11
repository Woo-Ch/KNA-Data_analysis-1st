import numpy as np

# 합계와 평균(mean)
s = np.array([70, 72, 71, 95, 73])
print(s.sum())  # 381 # 합계
print(s.mean())  # 76.2 # 평균
print(np.median(s))  # 72.0 # 중앙값

# 최대/최소 범위
print(s.max())  # 95
print(s.min())  # 70
print(s.max() - s.min())  # 25

# 분산
stable = np.array([70, 71, 70, 72, 71])
unstable = np.array([60, 85, 65, 95, 70])
print(stable.var())  # 0.5599999999999999
print(round(stable.var(), 2))  # 0.56

print(unstable.var())  # 170.0
print(round(unstable.var(), 2))  # 170.0

# 표준편차
s2 = np.array([70, 72, 71, 95, 73])
print(round(s2.var(), 2))  # 89.36
print(round(s2.std(), 2))  # 9.45

# axis 개념 (형과 열의 방향)
mat = np.array([[70, 2.1], [72, 2.3]])

print(mat.mean())  # 36.6
print(mat.mean(axis=0))  # [71.   2.2] # 열
print(mat.mean(axis=1))  # [36.05 37.15] # 행
