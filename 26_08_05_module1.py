# 수학 관련 모듈을 불러옵니다
import math

print(0)

# 해당 모듈이름.함수() 식으로 호출해야 한다
# math.sqrt  ->  제곱근 구하기
result = math.sqrt(16)
print(result)  # 4.0


# 수학 관련 모듈에서 sqrt 기능만 불러옵니다
# math라는 모듈을 다 가져오는게 아니라 그 안에 있는 sqrt만 뽑아오는 기능
from math import sqrt

result = sqrt(25)
print(result)  # 5.0

print("=" * 30)

# math라는 모듈 이름 다 쓰기 귀찮아서 줄여봅시다
import math as mt

# 별칭으로 가져온 모듈 이름을 언급해봅시다
result = mt.sqrt(36)
print(result)  # 6.0

# datetime 모듈을 가져옵니다
# import datetime # 이렇게 부르거나
import datetime as dt  # 넘 길어서 줄였음

# datetime의 now()는 현재의 지역 날짜와 시간을 반환합니다.
now = dt.datetime.now()
print(now)  # 2026-08-05 11:19:51.993955  ->  현재 년도, 날짜 시간 알려줌
print(type(now))  # <class 'datetime.datetime'>

# 실습1. import 세 방식으로 모듈 가져오기
# import 모듈명으로 통째로 가져와 모듈명.기능()으로 사용
import math

result1 = math.sqrt(16)
print(result1)  # 4.0

# from 모듈 import 기능으로 일부만 가져와 모듈명 없이 사용
from math import sqrt

result2 = sqrt(16)
print(result2)  # 4.0

# import 모듈 as 별명 으로 별명.기능() 으로 사용
import math as mt

result3 = mt.sqrt(16)
print(result3)  # 4.0
