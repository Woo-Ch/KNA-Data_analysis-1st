# 실습2. 다중 매개변수로 센서값 계산하기


def machine_stats(name, temp):
    print(f"{name} {temp} 도")


machine_stats("모터", 78)  # 모터 78 도
machine_stats("펌프", 92)  # 펌프 92 도

machine_stats(78, "모터")  # 78 모터 도
machine_stats(92, "펌프")  # 92 펌프 도
