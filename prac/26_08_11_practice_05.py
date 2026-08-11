# 실습5. 조건별 개수와 비율 세기
# 조건을 만족하는 값의 개수와 전체 대비 비율 계산
import numpy as np

# 토크 배열 준비
torque = np.array([42.8, 46.3, 49.4, 4.6, 41.9, 65.7, 40.2, 60.7])

# 비교 조건으로 참, 거짓 불리언 배열 생성
high = torque > 50  # 문제에서 요구하는 코드
print(high)  # [False False False False False  True False  True]

print(torque[torque > 50])  # [65.7 60.7] # 참고 코드

# 불리언 배열의 합(sum)으로 개수, 평균(mean)으로 비율 계산
print(high.sum())  # 2 (True = 1, False = 0으로 합산)
print(round(high.mean(), 2))  # 0.25, 소수점 이하 2자리까지 나오도록 처리

# 예상 결과
# 조건을 만족하는 값의 개수와 비율이 출력
