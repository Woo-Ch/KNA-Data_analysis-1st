# 선택 실습3. os로 폴더 목록 살펴보기

# 1단계. os 모듈을 import

import os

# 2단계. getcwd로 현재 작업 폴더를 확인

check = os.getcwd()

print(check)  # C:\Users\Visitor\Desktop\KNA-Data_analysis-1st

# 3단계. listdir로 폴더 안 목록을 변수에 담기

file_list = os.listdir()

print(file_list)

# 4단계. for로 목록을 하나씩 출력하고 csv만 골라 출력

for file_name in file_list:
    if ".csv" in file_name:
        print(file_name)  # 08_press.csv

# 완료!
