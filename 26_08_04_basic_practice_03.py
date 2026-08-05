# 실습3. 키워드 인자로 함수 호출하기


def machine_stats(name="모터", temp=78):
    print(name, temp)


machine_stats()  # 모터 78

machine_stats(name="펌프", temp=92)  # 펌프 92

machine_stats(temp=92, name="펌프")  # 펌프 92

machine_stats("펌프", temp=92)  # 펌프 92
