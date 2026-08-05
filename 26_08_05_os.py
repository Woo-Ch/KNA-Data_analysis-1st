# 표준 라이브러리의 os 모듈 활용
import os

# os.getcwd() 는 현재 작업 디렉토리를 문자열로 반환시켜준다
current_working_directory = os.getcwd()
print(current_working_directory)
# C:\Users\Visitor\Desktop\KNA-Data_analysis-1st


import os

file_list = os.listdir()
print(file_list)  # 해당 경로에 있는 파일 리스트들을 보여줌.

for file_name in file_list:
    print(file_name)
# 이렇게 출력하면 하나하나 나열되서 나오게 됨. 가독성 업

print("==================================================")

# 파일이 존재하는지 알아봅시다
# 운영체제(윈도/맥/리눅스) 마다 경로를 나타내는 방법이 달라서
# 상황에 맞게 경로문자열을 만들어주는 os의 함수를 사용합시다
path = os.path.join("data", "08_press.csv")
print(path)

# 실제로 경로문자열을 따라서 찾아가면
# 해당 파일이 있는지 알아봅시다: True/False
if os.path.exists(path):
    print(f"파일있음: {path}")  # 파일있음: data\08_press.csv

# 실습3. os로 폴더 목록 살펴보기
# os 모듈을 import
import os

# getcwd로 현재 작업 폴더를 확인
check = os.getcwd()
print(check)  # C:\Users\Visitor\Desktop\KNA-Data_analysis-1st

# listdir로 폴더 안 목록을 변수에 담기
list_file = os.listdir()
print(list_file)

# for로 목록을 하나씩 출력하고 csv만 골라 출력
for list_name in list_file:
    if ".csv" in list_name:
        print(list_name)  # 08_press.csv

