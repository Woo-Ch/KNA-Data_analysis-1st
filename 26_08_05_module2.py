# math 표준 라이브러리
import math

print(math.sqrt(9))  # 3.0  # 제곱근값
print(math.ceil(4.2))  # 5  # 올림값
print(2**3)  # 8  # 거듭제곱은 math 모듈 사용 안함

# math에서 sqrt, ceil 두개만 사용한다면 이렇게 써도 됩니다
from math import sqrt, ceil

# 위에서 가져온 math 함수 사용 예제입니다
print(sqrt(9))  # 3.0
print(ceil(4.2))  # 5

print("=" * 30)

# 표준 라이브러리의 random 모듈
import random  # 모듈은 코드 작성 전 제일 위에다가 모아서 작성하는 좋음

# 중간에 모듈을 작성하는 것은 극히 드물다.

print(random.randint(1, 10))  # 1~10 의 숫자중 하나를 랜덤으로 뽑아냄
print(random.choice(["정상", "경고", "위험"]))  # 셋 중 무작위

print("=" * 30)

# 표준 라이브러리의 datetime 모듈
import datetime
import datetime  # 중복해서 모듈을 불러온다고 해도 오류 발생 하지 않는다

# datetime 모듈 안의 datetime 클래스에서 지원하는 now() 함수 호출
now = datetime.datetime.now()
print(now)  # 현재 날짜, 시간 출력

print("=" * 30)

# 모듈 도움말 보기: 참고만 하고 구글링한 웹사이트에서 봅시다!
# dir(math)
# help(math.sqrt)

# 실습2. 표준 라이브러리로 센서값 만들기
import random

result1 = random.randint(1, 15)
print(result1)

from math import sqrt

result2 = sqrt(result1)
print(result2)

print("=" * 30)


# 절대경로와 상대경로
# 절대경로의 예 : C"\Users\admin\바탕화면\sample\code.py
# 만약 C"\Users\admin\바탕화면\sample\code.py 폴더에 터미널을 연 상태에서
# code.py 코드를 실행하고 싶다면
# python code.py

# 위 code.py 언급부분은 사실 상대경로를 의미한다
# 그래서 절대경로로 지정해줘도 똑같이 실행될 것이다.
# python C"\Users\admin\바탕화면\sample\code.py

# 현재 경로에 있는 해당 파일이란걸 더 강조하는 상대경로 지정으로 써도 된다
# python ./code.py

# 만약 C"\Users\admin\바탕화면\sample 아닌
# C"\Users\admin\바탕화면\example 폴더 경로에서 위 코드를 실행하고 싶다면
# 절대경로 : python C"\Users\admin\바탕화면\sample\code.py
# 상대경로 : python ..\sample\code.py

# ===============================================
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
