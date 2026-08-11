# 실습3. 센서값 정규화하기
# 목표: 회전수 배열을 0과 1 사이 값으로 정규화
import numpy as np

# 회전수 측정 배열 준비
rpm = np.array([1551, 1408, 1498, 1433, 1425, 1558, 2861, 1410])

# 최솟값과 최댓값을 min, max로 확인
print(rpm.min())  # 1408
print(rpm.max())  # 2861

# 정규화 공식을 브로드캐스팅으로 적용해 변환
# 정규화 공식
# 정규화된X = (비교대상 - 최소값) / (최대값 - 최소값)
rpm_min = rpm.min()
rpm_max = rpm.max()
normalized = (rpm - rpm_min) / (rpm_max - rpm_min)
print(normalized)
# [0.09841707 0.         0.06194081 0.01720578 0.01169993 0.10323469
#  1.         0.00137646]
# 소수점 이하값이 너무 길어진다면 numpy 배열에서 제공하는 round 기능을 활용
print(np.round(normalized, 2))  # [0.1  0.   0.06 0.02 0.01 0.1  1.   0.  ]
