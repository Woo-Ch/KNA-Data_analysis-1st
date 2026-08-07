# 선택 실습4. 함수 안에서 입력값 검증하기

# 1단계. 입력 값을 받는 함수를 정의
# 2단계. try에서 float로 변환해 검증
# 3딘계. 변환 실패시 except로 안내하고 기본값 처리
# 4단계. 정상·비정상 입력을 각각 넣어 확인


def check_value(temp, vib):
    try:
        temp = float(temp)
        vib = float(vib)

        if temp < 0 or temp > 100:
            raise ValueError("온도가 정상 범위를 벗어났습니다.")

        if vib < 0 or vib > 5:
            raise ValueError("진동이 정상 범위를 벗어났습니다.")

        print("정상 입력입니다.")
        print(f"온도: {temp}")
        print(f"진동: {vib}")

    except ValueError:
        print("잘못된 입력입니다.")


temp_input = input("온도를 입력해주세요: ")
vib_input = input("진동을 입력해주세요: ")

check_value(temp_input, vib_input)
