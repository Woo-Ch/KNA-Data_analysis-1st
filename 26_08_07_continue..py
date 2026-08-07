# 반복문 안에서 예외처리

my_list = ["123", "456", "영크크", "21", "11"]

# 문제 발생경우를 세어봅시다
problems = 0

for text in my_list:
    # 반복을 하는 중에 문제가 생긴 경우만 견너뛰고
    # 계속 반복을 이어서 진행시키기

    try:
        my_number = int(text)
    except:
        # print("문제발생")
        # 문제가 생겼다면 더 이상 반복문 안의 출력까지 이어가면 안되겠다
        # 그래서 여기서 끊고 다음 내용 처리하게 반복문 넘기기

        # 갈 때 가더라도 문제상황 카운팅 정도는 좋찮아
        problems += 1

        continue

    print(my_number)

print(f"{problems}개는 문제가 있어서 건너뜀")
