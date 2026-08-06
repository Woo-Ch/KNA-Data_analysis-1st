# 실습4. csv.reader로 csv 읽기

# 1단계. csv 모듈을 import

import csv
import os

csv_path = os.path.join("data", "08_press.csv")

# 2단계. with open으로 csv를 읽기 모드 utf-8로 열기
# 3단계. csv.reader로 reader 객체를 만들기
# 4단계. for 로 각 행(리스트)을 하나씩 꺼내 출력

with open(csv_path, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# 완료!!
