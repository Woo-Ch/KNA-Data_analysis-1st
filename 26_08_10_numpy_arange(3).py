import numpy as np

# 0부터 4까지 생성
under_five = np.arange(5)
print(under_five)  # [0 1 2 3 4]

# 0부터 8까지 2간격 (8보다 큰 숫자가 만들어지면 덧붙이지 않고 끝)
gab_two = np.arange(0, 9, 2)
print(gab_two)  # [0 2 4 6 8]
