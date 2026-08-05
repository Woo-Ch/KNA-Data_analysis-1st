# 실습1. import 세 방식으로 모듈 가져오기

# 1단계. import 모듈명으로 통째로 가져와 모듈명.기능() 으로 사용
import math

result = math.sqrt(16)

print(result)  # 4.0

# 2단계. from 모듈 import 기능으로 일부만 가져와 모듈명 없이 사용
from math import sqrt

result = sqrt(16)

print(result)  # 4.0

# 3단계. import 모듈 as 별명으로 별명.기능()으로 사용
import math as mt

result = mt.sqrt(16)

print(result)  # 4.0

# 세 방식의 출력이 모두 같음!
