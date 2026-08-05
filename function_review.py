# 함수의 기본 예제
def say_hello():
    pass  # 아무일도 안하는 코드


def say_hi():
    print("안녕하세요")


# 함수는 선언된(def) 후에 호출돼야 한다.
say_hi()  # 안녕하세요


# 매개변수를 사용하면 더 다양한 일을 할 수 있습니다
def show_hello(name):
    print(f"{name}님 안녕하세요!")


show_hello("MW")  # MW님 안녕하세요!
show_hello("JR")  # JR님 안녕하세요!
show_hello("JH")  # JH님 안녕하세요!


# 매개변수는 여러 값을 받을 수 있고
def show_hi(name, message):
    print(f"{message}, {name}")


show_hi("MW", "하이요")  # 하이요, MW
show_hi("JR", "방가요")  # 방가요, JR


# 매개변수에는 따로 안알려주면 기본값을 적용할 수도 있습니다
def show_greeting(name, message="안녕하세요"):
    print(f"{message}, {name}")


show_greeting("MW")  # 안녕하세요, MW
show_greeting("MW", "하이요")  # 하이요, MW
show_greeting("MW", message="방가요")  # 방가요, MW
show_greeting("MW")  # 안녕하세요, MW
