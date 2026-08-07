# 종합실습
## 1단계 csv 읽기

import os
import csv

csv_path = os.path.join("data", "09_ict_inspection_dirty.csv")


def output():
    try:
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)

            header = next(reader)
            rows = []

            for row in reader:
                rows.append(row)

            print(len(rows))
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다")
        return [], []


output() # 21


