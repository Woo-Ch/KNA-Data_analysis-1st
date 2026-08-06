# 선택 실습3. 구체적 예외로 입력 검증하기

# 1단계. 입력을 int로 바꾸는 코드를 try에 넣기
# 2단계. ValueError를 except로 잡아 안내
# 3단계. 여 러except로 ZeroDivisionError도구 분해 처리
# 4단계. 잘못된 입력을 넣어 프로그램이 멈추지 않는지 확인

origin = input("입력: ")

try:
    user_input = int(origin)
    calc = 10 / user_input
    print(calc)
except ValueError:
    print("숫자를 입력해 주세요")
except ZeroDivisionError:
    print("0으로 나눗셈은 불가능합니다")

# 완료!!
