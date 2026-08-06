# 실습6. csv 읽어 조건 저장하기

# 1단계. csv를 import

import csv
import os

csv_path = os.path.join("data", "08_press.csv")

result = []

# 2단계. csv.reader를 읽고 첫 줄 헤더는 건너뛰기

with open(csv_path, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    # 3단계. 값을 float로 변환해 기준(90) 초과 행만 리스트에 모으기
    for row in reader:
        if float(row[4]) > 90:
            result.append(row)


# 4단계. csv.writer로 모은 행들을 새 csv에 저장

save_path = os.path.join("data", "90over.csv")

with open(save_path, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(result)

# 완료!!
