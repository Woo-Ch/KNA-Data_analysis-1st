# 실습3. 여러 파일 묶어 처리하기

# 다음과 같은 식의 리스트를 만들어 반복문으로 처리해봅시다
# for문으로 리스트의 문자열을 꺼내어 해당 이름의 파일들을 열어보기 시도하면 됩니다
# file_names = ["08_press.csv", "09_ict.csv", "09_ict_dirty.csv"]

# 1단계. 여러 파일 이름을 반복
# 2단계. try에서 파일을 열어 처리
# 3단계. 없는파일(FileNotFoundError)시 continue로 건너뛰기
# 4단계. 처리한 파일수를 세어 출력

import os

file_name = ["08_press.csv", "09_ict_inspection.csv", "None_file.csv"]

file_count = 0

for file in file_name:
    try:
        file_path = os.path.join("data", file)

        f = open(file_path, "r", encoding="utf-8")
        file_count += 1
        f.close()

    except FileNotFoundError:
        continue

print(f"처리한 파일수: {file_count}")

# 완료!!