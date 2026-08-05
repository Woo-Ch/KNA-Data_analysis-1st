# 선택 실습6. 폴더에서 csv 파일만 골라내기

# 1단계. os를 import하고 listdir로 폴더 목록을 구하기

import os

file_list = os.listdir()
print(file_list)

# 2단계. for-if로 .csv로 끝나는 이름만 빈 리스트에 모으기

csv_list = []

for file_name in file_list:
    if ".csv" in file_name:
        csv_list.append(file_name)

# 3단계. 모은 csv마다 path.join으로 전체 경로를 만들기

for file_name in csv_list:
    csv_path = os.path.join(os.getcwd(), file_name)

# 4단계. 골라낸 csv 목록을 출력

print(csv_list)

# 완료!!
