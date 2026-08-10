# 2차원 인덱싱

import numpy as np

data = np.array([[70, 2.1], [72, 2.3]])

print(data)
# [[70.   2.1]
#  [72.   2.3]]
print(data.dtype)  # float64

# 기존 리스트처럼 특정 위치 지정해 콕 찝어오기
print(data[0][1])  # 2.1

# 대부분의 numpy의 배열은 수학공식 같은 식으로 위치를 지정한다
# 0행[row] 1열[column]
print(data[0, 1])  # 2.1
