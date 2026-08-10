# 실습 5. 자료형 확인과 변환하기

import numpy as np

data = np.array([1334.232, 234123.23, 34523.234])

# dtype으로 현재 자료형 확인
print(data.dtype)  # float64

# astype으로 정수형으로 변환한 새 배열 출력
converted_data = data.astype(int)
print(converted_data)  # [  1334 234123  34523]
