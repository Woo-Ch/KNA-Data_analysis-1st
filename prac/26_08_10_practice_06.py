# 실습 6. 배열 모양 바꾸기

import numpy as np

# 연속 정수 배열을 arange로 생성
numbers = np.arange(10)
print(numbers)  # [0 1 2 3 4 5 6 7 8 9]


# 값 개수에 맞는 행, 열을 정해 reshape으로 형태 변환
numbers_reshape = numbers.reshape(2, 5)


# 바뀐 배열 출력
print(numbers_reshape)
# [[0 1 2 3 4]
#  [5 6 7 8 9]]
