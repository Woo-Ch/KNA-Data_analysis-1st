# csv.DictReader

import os
import csv

csv_path = os.path.join("data", "08_press.csv")

with open(csv_path, "r", encoding="utf-8") as f:
    # DictReader는 첫 줄은 컬럼 이름으로 판단하고
    # 각 row를 해당 컬럼이름들을 key로 하는 딕셔너리로 만들어 준다
    reader = csv.DictReader(f)

    for row in reader:
        print(row["설비ID"], row.get("시각"))

