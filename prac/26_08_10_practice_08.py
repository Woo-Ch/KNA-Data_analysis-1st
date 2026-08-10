# 실습 8. 배열 생성부터 정리까지

import numpy as np

# [최종결과]
# 형태와 자료형 확인 후 3행 2열 표로 정리된 배열 출력
# 최종형태 shape : (3, 2)
# 최종형태 size : 3 * 2 = 6

# 센서 측정값을 np.array로 배열 생성
sensor_value = np.array([1.2, 3.5, 4.9, 8.2, 2.3, 1.5])


# shape과 dtype으로 구조 확인
print(sensor_value.shape)  # (6,)
print(sensor_value.dtype)  # float64


# reshape으로 분석을 표 형태로 정리한 뒤 출력
sensor_value_reshape = sensor_value.reshape(3, 2)
print(sensor_value_reshape)
# [[1.2 3.5]
#  [4.9 8.2]
#  [2.3 1.5]]
