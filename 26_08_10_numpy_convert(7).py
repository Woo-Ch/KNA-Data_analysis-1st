import numpy as np

# 형변환(astype)
# 예를들어 아래의 float들로 가득한 배열이 있다면
convertable = np.array([3.14, 3.7, 1.23])
print(convertable.dtype)  # float64

# int들로 가득한 배열로 알아서 바꿔준다
converted = convertable.astype(int)
print(converted)  # [3 3 1]
print(converted.dtype)  # int64
