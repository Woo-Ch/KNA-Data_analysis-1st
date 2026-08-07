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


## 4단계 불량 방어
def clean_data(rows):
    normal_rows = []
    bad_rows = []

    row_number = 1

    for row in rows:
        row_number += 1

        try:
            # 부품명이 없는 경우
            if row[1] == "":
                raise ValueError("부품명이 없습니다.")

            # 숫자로 변환
            measure = float(row[2])
            upper = float(row[4])
            lower = float(row[5])

            # 정상 범위 검사
            if measure < lower or measure > upper:
                raise ValueError("측정값이 정상 범위를 벗어났습니다.")

            # 여기까지 왔으면 정상 데이터
            normal_rows.append(row)

        except (ValueError, IndexError) as e:
            bad_rows.append([row_number, str(e)])

            print(
                f"{row_number}번 줄 제외:",
                e,
            )

            continue

    print("정상 데이터:", len(normal_rows), "개")
    print("불량 데이터:", len(bad_rows), "개")

    return normal_rows, bad_rows


normal_rows, bad_rows = clean_data(rows)
