# ==========================================
# 종합실습
# ==========================================

import os
import csv

csv_path = os.path.join("data", "09_ict_inspection_dirty.csv")
report_path = os.path.join("data", "inspection_report.txt")


# ==========================================
# 1단계. CSV 읽기
# ==========================================
# 1. csv 파일을 읽는 함수 정의
# 2. 헤더와 데이터 행을 분리
# 3. 데이터 행 수 출력
# 4. 파일이 없으면 FileNotFoundError 처리
# 5. 파일이 없을 경우 빈 header, 빈 rows 반환


def read_csv():
    try:
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)

            header = next(reader)
            rows = []

            for row in reader:
                rows.append(row)

            print("헤더:", header)
            print("데이터 행 수:", len(rows))

            return header, rows

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
        return [], []


# ==========================================
# 2단계. 부품별 조건 분류
# ==========================================
# 1. 부품별 데이터를 담을 빈 딕셔너리 생성
# 2. 각 행에서 부품명(row[1]) 가져오기
# 3. 처음 보는 부품이면 빈 리스트 생성
# 4. 해당 부품의 리스트에 행 추가
# 5. 부품별 데이터 개수 출력


def group_parts(rows):
    part_dict = {}

    for row in rows:
        part = row[1]

        if part not in part_dict:
            part_dict[part] = []

        part_dict[part].append(row)

    for part in part_dict:
        print(part, ":", len(part_dict[part]), "개")

    return part_dict


# ==========================================
# 3단계. 통계 함수
# ==========================================
# 1. 숫자 데이터가 들어올 리스트 생성
# 2. 값을 하나씩 float로 변환
# 3. 숫자가 아닌 값은 continue로 건너뛰기
# 4. 정상 숫자만 리스트에 저장
# 5. 값이 하나도 없으면 None 반환
# 6. 개수, 평균, 최솟값, 최댓값 반환


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


# ==========================================
# 4단계. 불량 방어
# ==========================================
# 1. 데이터를 한 행씩 확인
# 2. 부품명이 없으면 예외 발생
# 3. 측정값, 상한치, 하한치를 float로 변환
# 4. 숫자로 변환할 수 없는 값은 제외
# 5. 정상 범위를 벗어난 측정값은 raise로 예외 발생
# 6. 정상 행과 불량 행을 각각 저장


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


# ==========================================
# 5단계. 리포트 저장
# ==========================================
# 1. 리포트 내용을 담을 리스트 생성
# 2. 전체 정상/불량 개수 기록
# 3. 부품별 측정값 통계 기록
# 4. 불량 행 번호와 이유 기록
# 5. txt 파일에 한 번에 저장


def save_report(normal_rows, bad_rows, part_dict):
    report = []

    report.append("===== ICT 검사 분석 리포트 =====\n")
    report.append(f"정상 데이터 수: {len(normal_rows)}\n")
    report.append(f"불량 데이터 수: {len(bad_rows)}\n")
    report.append("\n")

    report.append("===== 부품별 측정값 통계 =====\n")

    for part in part_dict:
        measure_list = []

        for row in part_dict[part]:
            measure_list.append(row[2])

        result = statistics(measure_list)

        if result is None:
            report.append(f"{part}: 계산 가능한 데이터 없음\n")
            continue

        count, avg, min_value, max_value = result

        report.append(
            f"{part} | 개수: {count} | "
            f"평균: {avg:.2f} | "
            f"최소: {min_value:.2f} | "
            f"최대: {max_value:.2f}\n"
        )

    report.append("\n")
    report.append("===== 불량 데이터 =====\n")

    for bad in bad_rows:
        report.append(f"{bad[0]}번 줄 | 이유: {bad[1]}\n")

    with open(report_path, "w", encoding="utf-8") as f:
        for line in report:
            f.write(line)

    print("리포트 저장 완료")


# ==========================================
# 6단계. 통계 검증
# ==========================================
# 1. 부품별 정상 데이터 개수를 더함
# 2. 전체 정상 데이터 개수와 비교
# 3. 같으면 True 출력


def check_count(part_dict, normal_rows):
    part_total = 0

    for part in part_dict:
        part_total += len(part_dict[part])

    result = part_total == len(normal_rows)

    print("부품별 개수 합:", part_total)
    print("전체 정상 개수:", len(normal_rows))
    print("검증 결과:", result)

    return result


# ==========================================
# 함수 실행
# ==========================================

# 1단계
header, rows = read_csv()

# 2단계 - 원본 데이터 부품별 분류
raw_part_dict = group_parts(rows)

print("------------------------------")

# 4단계 - 불량 제거
normal_rows, bad_rows = clean_data(rows)

print("------------------------------")

# 정상 데이터만 다시 부품별 분류
part_dict = group_parts(normal_rows)

print("------------------------------")

# 3단계 통계 함수 사용 예시
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

print("------------------------------")

# 5단계
save_report(normal_rows, bad_rows, part_dict)

print("------------------------------")

# 6단계
check_count(part_dict, normal_rows)
