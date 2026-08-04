# print 함수를 생각해봅시다
print("안녕하세요")

first_name = "MW"
last_name = "C"
print(first_name)
print(last_name)
print(first_name, last_name)

# 위와 같이 똑같은 print를 호출에도
# 다양한 방법의 호출이 가능합니다.
# 그 원리를 알려면
# 우리가 직접 함수들을 만들 수 있어야 합니다.

# 에러(Error)의 종류
# 1. 실행중에 오류 (Runtime Error) - 작동 중단됨
# 2. 논리적 오류 - 작동은 잘 되는데, 결과적으론 문제가 있어 고쳐야 함
# : 우리는 함수 이름에 걸맞는 동작만 잘 되도록 만들어야합니다!


# 간단한 인사메시지 보여주기 함수를 만들기
# ":"으로 끝나는 줄의 뜻은 "이 다음 줄부터 들여쓴 내용은 한 묶음"
def say_hello():
    print("안녕하세요")


# 위에서 만든 함수는 이렇게 호출해야만 실행됩니다.
say_hello()  # 안녕하세요


print("=====3교시=====")


# 함수 안에서 벌어지는 일들을 만들어봅시다
def show_number():
    my_number = 44
    print(f"my_number: {my_number}")


# 위 함수를 실행해봅시다.
show_number()  # 44

# 여기서도 my_number 값을 정해봅시다
# 아랫줄의 my_number는 show_number함수 안의 my_number와 다른 존재
my_number = 24
show_number()  # 44

# 그래서 함수안의 my_number 데이터가 영향을 끼치는 범위를
# 전문용어로 스코프(scope)라고 부른다

# 함수는 호출되기 전에 만들어져야 합니다
# show_title() # NameError


def show_title():
    print("함수 배우기")


show_title()  # 정상 실행


# 실습1. 첫 함수 만들고 호출하기. 답안.
def start_checking():
    print("점검을 시작합니다")


start_checking()  # 점검을 시작합니다
start_checking()  # 점검을 시작합니다


# 함수가 호출되면 그 안의 코드는 매번 새롭게 시작된다
def show_counter():
    # count = count + 1 # 기존 count라는 존재는 모른다고 error
    count = 0
    print(count)
    # 이 함수가 종료되면 count를 포함한 이 함수 안의 데이터는 모두 사라짐


show_counter()  # 0
show_counter()  # 0

# 각 함수의 이름은 이름에 걸맞는 역할만 해줘야 한다


def show_students():
    print("학생: 짱구")
    print("학생: 철수")
    print("학생: 훈이")


def show_teacher():
    print("선생님: 채송화")


show_students()
show_teacher()


def show_classroom():
    show_teacher()
    show_students()


show_classroom()
# 다단계 호출

print("===== 4교시 =====")

# [상식]
# 특정 부분의 코드가 문제 없지만
# 다른 부분과 예상치 못한 영향을 주고받는다면?

# 코드 중복과 함수화

print("압축기A 온도 확인 중")
print("결과를 기록합니다")
print("펌프1 온도 확인 중")
print("결과를 기록합니다")

# 위와 같은 식의 코드를 여기저기 복사-붙여넣기 하면
# 언젠가 사람의 실수로 사고가 생길 수 있다


# 실습2. 반복 코드를 함수로 정리하기 - 강사님과 같이 진행
def start_check():
    print("점검을 시작합니다")
    print("안전 장비를 확인하세요")
    print("기록을 준비하세요")


start_check()  # 압축기 A
start_check()  # 펌프1

print("========================================")


# 함수의 호출 결과 예측하기
# 실습3. 함수 실행 흐름 추적하기
def say_hi():
    print("안녕하세요")


say_hi()
say_hi()

# 실습4. 함수로 설비 점검 자동화하기
# 구분선과 점검안내 2줄이 설비마다 반복 출력
# 1. 구분선을 출력하는 함수를 정의
# 2. 점검 안내 여러 줄을 출력하는 함수를 정의
# 3. 두 함수를 설비마다 순서대로 호출
# 4. 실행해 각 설비마다 같은 안내가 반복되는지 확인
# 예상결과: 구분선과 점검 안내 2줄이 설비마다 반복 출력


def print_line():
    print("=" * 20)


def print_check():
    print("점검을 시작합니다")
    print("기록을 준비하세요")


# 장비1에 대한 함수 호출
print_line()
print_check()

# 장비2에 대한 함수 호출
print_line()
print_check()

