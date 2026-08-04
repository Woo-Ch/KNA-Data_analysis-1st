# 지금까지 배운 내용을 활용해서
# 재미있는 함수 만들기 예제

import random

groups = ["에스파", "하트2하트", "리센느", "태연", "엔믹스"]

# 랜덤 뽑기!
my_group = random.choice(groups)
print(my_group)


def random_group():
    group_details = [
        {"이름": "에스파", "리더": "카리나"},
        {"이름": "엔믹스", "리더": "해원"},
        {"이름": "리센느", "리더": "원이"},
    ]

    my_group = random.choice(group_details)

    return my_group.get("이름"), my_group.get("리더")


group_name, group_leader = random_group()
print(f"{group_name}의 리더는 {group_leader}입니다")

# 여러분의 활동을 원합니다
# 어제처럼 주변 3~4인과 함께 코드를 만드세요
# 가봤거나, 가보고싶은 여행지 정보를 모아봅시다 (최소 5개 이상)
# 함수를 호출하면 랜덤으로 해당 여행지의 국가이름과 수도
# "환영합니다! 000 나라의 수도 000 입니다" 출력
