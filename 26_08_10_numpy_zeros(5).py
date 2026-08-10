import numpy as np

# 0으로 채우기
block_zeros = np.zeros(5)
print(block_zeros)  # [0. 0. 0. 0. 0.]

# 7으로 채우기
block_seven = np.full(4, 7)
print(block_seven)  # [7 7 7 7]

# 명시적으로 7.0처럼 float값을 지정해줘야
# float 타입 값으로 채워지는 배열이 만들어진다.
block_seven = np.full(4, 7.0)
print(block_seven)  # [7. 7. 7. 7.]
