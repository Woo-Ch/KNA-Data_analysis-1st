# 실습5. csv.writer로 csv 쓰기

# 1단계. csv를 import

import csv
import os

csv_path = os.path.join("data", "prac_result.csv")

# 2단계. with open으로 w, utf-8, newline 옵션으로 열기
# 3단계. csv.writer 로 writer 객체를 만들기
# 4단계. writerow로 헤더와 각 데이터 행을 쓰기

with open(csv_path, "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["설비명", "온도", "압력"])
    writer.writerow(["PUMP_A", "78", "30"])

# 완료!!
