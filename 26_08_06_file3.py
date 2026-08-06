import os
import csv
import sys

csv_path = os.path.join("data", "result.csv")

with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["시각", "설비"])
    writer.writerow(["09:00", "PUMP-01"])

# 앞서 사용했던 write와 다른 점은
# 줄바꿈을 하기 위해 \n을 사용하지 않은 점.
# 내용을 하나만 입력한 것이 아닌 리스트로 입력한 점.

# result.csv 파일에 띄어쓰기가 생기는 이유
# 윈도우에서만 그럼
# \n이 더 들어가는 일종의 버그
# 해결방법은
# with open(csv_path, "w", newline="", encoding="utf-8") as f:
# with open(csv_path, "w", encoding="utf-8", newline="") as f:
# 위와 같이 newline=""을 작성해주면 해결된다.
# newline=""들어가는 위치는 상관없음
