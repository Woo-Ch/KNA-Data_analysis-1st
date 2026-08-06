import os
import csv

csv_path = os.path.join("data", "08_press.csv")

with open(csv_path, "r", encoding="utf-8") as f:
    # print(f.readlines()) # 이제 csv 전문가에게 맡깁시다
    reader = csv.reader(f)

    # DictReader가 아닌 그냥 reader를 사용한다면
    # 보통 csv파일의 첫줄인 헤더줄도 읽어버린다
    # reader에게 첫줄은 건너뛰라고 말하는 방법이 필요하다
    header = next(reader)
    # header는 따로 리스트로 챙겨진다
    # ["설비ID", "시각", "진동X", "진동Y", "전류", "상태"]

    for row in reader:
        print(row)  # 각 행(row)마다 리스트로 출력됨
