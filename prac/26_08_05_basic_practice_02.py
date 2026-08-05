# 실습2. 표준 라이브러리로 센서값 만들기

# 1단계. random 모듈을 import
import random

# 2단계. randint로 무작위 센서값을 만들어 출력

random_list = random.randint(1, 20)

print(random_list)  # 실행할때마다 출력되는 값 다름 확인

# 3단계. math 모듈로 그 값을 가공(제곱근)

import math

random_list_sqrt = math.sqrt(random_list)

print(random_list_sqrt)

# 4단계. 다시 실행하면 값이 달라지는지 확인 완료!!
