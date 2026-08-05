# 실습5. datetime으로 점검 기록 남기기

# 1단계. os와 datetime을 import

import os
import datetime

# 2단계. listdir로 폴더 파일 수를 구하기

file_count = len(os.listdir("prac"))

print(file_count)  # 6

# 3단계. datetime.now로 현재 시각을 담기

now = datetime.datetime.now()

print(now)  # 2026-08-05 15:48:06.969782

# 4단계. f-string으로 파일 수와 시각을 한 문장으로 출력

print(f"파일 {file_count}개, 점검 시각 {now}")
# 파일 6개, 점검 시각 2026-08-05 15:48:59.730786

# 완료!
