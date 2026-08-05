# 실습4. os로 파일 존재 확인하기

# 1단계. os를 import

import os

# 2단계. path.join으로 폴더와 파일 이름을 이어 경로를 만들기

path = os.path.join("prac", "26_08_05_basic_practice_04.py")

print(path)  # KNA-Data_analysis-1st\26_08_05_basic_practice_04.py

# 3단계. path.exists로 그 경로가 있는지 참, 거짓 확인

print(os.path.exists("prac"))  # True
print(os.path.exists("26_08_05_basic_practice_04.py"))  # False
print(os.path.exists("prac/26_08_05_basic_practice_04.py"))  # True

# 4단계. if로 있으면, 없으면 다른 메시지 출력


def verdict(name):
    if os.path.exists(name) == True:
        print("파일 있음")
    else:
        print("파일 없음")


verdict("prac")  # 파일 있음

verdict("praccccc")  # 파일 없음

# 완료!!
