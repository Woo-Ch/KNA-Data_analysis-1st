# 학생들의 점수를 가져와서
# 각 학생별 합계와
# 모든 학생들의 평균 점수를 내는 코드
# 제출 안하는 실습
# 1. 실행 끝날 때 최고점 학생, 최저점 학생도 찾아서 출력해보세요
# 2. 실행 끝날 때 각 과목별 평균도 출력해보세요

import os
import sys
import csv

# 0. 미리 전체 합산 점수 낼 준비를 한다

students_count = 0
total_all = 0
total_kor = 0
total_eng = 0
total_math = 0

max_name = ""
max_total = 0

min_name = ""
min_total = 101  # 모든 학생 개별 평점수는 100점 이하일거라 보고 처리

# 1. 파일을 연다
file_path = os.path.join("data", "student_scores.csv")

if not os.path.exists(file_path):
    print("파일을 찾지 못했습니다.")
    sys.exit(1)

with open(file_path, "r", encoding="utf-8") as f:
    # 2. 파일 내용으로부터 리스트 데이터를 얻는다
    reader = csv.DictReader(f)

    for row in reader:
        name = row.get("\ufeff이름", "(이름없음)")
        kor = int(row.get("국어", "0"))
        eng = int(row.get("영어", "0"))
        math = int(row.get("수학", "0"))
        total = (kor + eng + math) / 3
        print(f"{name} | {kor} | {eng} | {math} | {total}")

        # 3. 점수 계산 (합계, 평균)
        students_count += 1
        total_all += total
        total_kor += kor
        total_eng += eng
        total_math += math

        # 3.5 최고점 학생인지 확인
        if total > max_total:
            max_name = name
            max_total = total

        # 3.5 최저점 학생인지 확인
        if total < min_total:
            min_name = name
            min_total = total


# 4. 결과를 화면에 보여주기
avg_all = total_all / students_count
avg_kor = total_kor / students_count
avg_eng = total_eng / students_count
avg_math = total_math / students_count

print(f"전체 {students_count}명 | 평균 {avg_all}점")
print(f"최고점 학생 {max_name} | 합계점수 {max_total}")
print(f"최저점 학생 {min_name} | 합계점수 {min_total}")
print(f"모든학생 국어 평균 {avg_kor}")
print(f"모든학생 영어 평균 {avg_eng}")
print(f"모든학생 수학 평균 {avg_math}")
