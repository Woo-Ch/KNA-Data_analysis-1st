# 종합실습
## 1단계 csv 읽기

import os
import csv

csv_path = os.path.join("data", "09_ict_inspection_dirty.csv")

rows = []


def output():
    try:
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)

            header = next(reader)

            for row in reader:
                rows.append(row)

            print(len(rows))
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다")
        return [], []


output()  # 21


## 2단계 조건 분류

part_dict = {}

for row in rows:
    part = row[1]

    if part == "":
        continue

    if part not in part_dict:
        part_dict[part] = []

    part_dict[part].append(row)

for part in part_dict:
    print(part, len(part_dict[part]))


## 3단계 통계 함수
def statistics(data):
    number_list = []

    for value in data:
        try:
            number = float(value)
            number_list.append(number)

        except ValueError:
            continue

    if len(number_list) == 0:
        return None

    count = len(number_list)
    avg = sum(number_list) / count
    min_value = min(number_list)
    max_value = max(number_list)

    return count, avg, min_value, max_value


for part in part_dict:
    measure_list = []

    for row in part_dict[part]:
        measure_list.append(row[2])

    result = statistics(measure_list)

    if result is not None:
        count, avg, min_value, max_value = result

        print(
            f"{part} | 개수: {count} | "
            f"평균: {avg:.2f} | "
            f"최소: {min_value:.2f} | "
            f"최대: {max_value:.2f}"
        )
