# 실습1을 위한 참고 코드
# 미국식 속도 (miles)를 우리가 쓰는 속도(km)로 변환시켜주는
# NumPy 배열 예제 코드

import numpy as np

miles = np.array([94.7, 104.5, 105.4])

# 속도(km/h) = 속도(mph) x 1.60934

print(miles * 1.60934)  # [152.404498 168.17603  169.624436]


# 실습1. 센서값 배열 만들기
import numpy as np

temps_C = np.array([30, 34, 38, 40])

# 화씨 변환 공식: F = °C × 1.8 + 32

print(temps_C * 1.8 + 32)  # [ 86.   93.2 100.4 104. ]
