origin = input("온도 : ")

print(f"입력한 온도는 {origin}")

try:
    temp = int(origin)
except ValueError:
    # ValueError인 상황이었다면 여기로 예외처리
    print("숫자 아니면 왜 절르 부르셨어요?")
    temp = 0
except TypeError:
    # TypeError인 상황이었다면 여기로 예외처리
    print("타입 문제는 전지구적 문제입니다.")


next_temp = temp + 10
print(f"10도만 더 높으면 {next_temp}")
