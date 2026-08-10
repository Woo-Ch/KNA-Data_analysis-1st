# 실습3을 위한 참고자료

# 측정 시간축 배열 만들기

import numpy as np

# 특정 시작 시각과 끝 시각을 정해서
# 특정 간격 시간들이 지난다면
# 언제 언제 체크포인트가 만들어지나를
# numpy의 배열로 알아보기

# 예를 들어 0초부터 60초 사이에
# 5초 간격으로 체크를 한다면
# 실제로는 몇초 몇초... 체크하는 지점이 생기나
# 알아보기
checks = np.arange(0, 60, 5)
print(checks)  # [ 0  5 10 15 20 25 30 35 40 45 50 55]


# 실습3. 측정 시간축 배열 만들기
import numpy as np

sec_gab1 = np.arange(0, 30, 5)
print(sec_gab1)  # [ 0  5 10 15 20 25]

sec_gab2 = np.arange(0, 30, 10)
print(sec_gab2)  # [ 0 10 20]
