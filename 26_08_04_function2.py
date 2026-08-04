# 인삿말 출력 함수 간단 버전
def say_hello():
    print("안녕하세요")


say_hello()  # 안녕하세요


# 인삿말 출력 함수 친근 버전
def say_hello_MW():
    print("안녕하세요, MW")


def say_hello_JR():
    print("안녕하세요, JR")


say_hello_MW()  # 안녕하세요, MW
say_hello_JR()  # 안녕하세요, JR

# 인사할 대상이 많아진다고 위 함수들을 더 만드는건 좀 아니지않나?
# 해결책은 하나의 함수에서 저 다양성을 다 대응해주는 것
# 그것이 바로 함수의 매개변수 활용


def say_hi(name):
    print(f"반갑습니다 {name}")


say_hi("MW")  # 반갑습니다 MW
say_hi("JR")  # 반갑습니다 JR

# 예제코드 : 특정 장비 이름을 알려주면 해당 장비의 체크를 시작 알림


def check(name):
    print(f"{name} 장비의 점검을 시작합니다")


check("압축기A")  # 압축기A 장비의 점검을 시작합니다
check("펌프B")  # 펌프B 장비의 점검을 시작합니다


# 매개변수가 2개 이상인 예제 - 덧셈
def calc_sum(number_a, number_b):
    # number_a = 1
    # number_b = 2
    total = number_a + number_b
    print(f"{number_a} + {number_b} = {total}")


calc_sum(3, 4)


# 매개변수가 2개 이상인 예제 - 장비 이름과 온도 정보 출력
def report(name, temp):
    # name = "압축기A"
    # temp = 75.3
    print(f"{name}의 온도는 {temp}도입니다.")


report("압축기A", 75.3)  # 압축기A의 온도는 75.3도입니다.
report("펌프B", 85.2)  # 펌프B의 온도는 85.2도입니다.

# 엉뚱하게 호출해봅시다
report(35.2, "보일러C")  # 35.2의 온도는 보일러C도입니다.
# 첫번째 매개변수는 무조건 name이 되고,
# 두번째 매개변수는 무조건 temp가 되니까
# 원하지 않는 결과가 나올 수도 있다

# 매개변수가 부족하거나 더 있으면?
# report("압축기A", 75.3, "가동중") # TypeError
# report("펌프B") # TypeError


# 키워드 인자
def report_keywords(name, temp):
    print(f"{name}의 온도는 {temp}도 입니다.")


# 키워드 인자 없이 호출
report_keywords("펌프A", 37.4)
report_keywords(37.4, "펌프A")  # 이 경우는 문제 발생

# 키원드 인자 사용해 호출하기 : 순서 바꿔 호출해 생기는 문제 근본 차단
report_keywords(name="펌프A", temp=37.4)  # 펌프A의 온도는 37.4도 입니다.
report_keywords(temp=37.4, name="펌프A")  # 펌프A의 온도는 37.4도 입니다.


print("=========================================")

# 반환값


# def add():
#     print("1 + 1 = 2")
#     return
#     print("1 + 1 = 2") # return 앞에 있는 것까지만 실행됨

# def add():
#     return # 바로 return 작성해서 빈함수 만들기도 가능


def add(a, b):
    total = a + b
    return total


print(add(1, 2))  # 3
print(add(11, 120))  # 131

# 여러번 같은 결과 호출해야한다면
# 차라리 변수에 담아서 쓰세요
result = add(1, 2)
print(result + 1)  # 4
print(result + 2)  # 5
print(result + 3)  # 6


# 평균 내는 함수 만들기
def calc_average(a, b):
    return (a + b) / 2


avg = calc_average(75.3, 88.0)
print(f"평균온도: {avg}")


print("===== 6교시 =====")


# 여러 값을 한 번에 반환하기
# 다음의 함수는 배열을 받아서 그 안의 최소값과 최대값을 동시에 return한다
def calc_min_max(values):
    minimum = min(values)  # 배열 안의 최소값 찾아 minimum에 담기
    maximum = max(values)  # 배열 안의 최대값 찾아 maximum에 담기
    return minimum, maximum  # 자동으로 튜플로 묶어서 반환됨


target_list = [1, 2, 3, 4, 5, 6]
result = calc_min_max(target_list)
print(result)  # (1, 6)
print(type(result))  # <class 'tuple'>

# 반환값을 언패킹으로 받기
# 함수의 결과를 받는 순간에
# 결과 튜플의 내용을 풀어서
# 개별 변수에 담아 사용하기
result_min, result_max = calc_min_max(target_list)
print("최소값 " + str(result_min))  # 최소값 1
print("최대값 " + str(result_max))  # 최대값 6

# return 반환값이 없는 함수를 호출해놓고
# 결과를 어디에 담겠다고 하면,
# 담기는 값은 None이 된다.


def say_great():
    print("만나서 반갑습니다")
    return


great = say_great()
print(great)  # None

# 실습5 (선택문제)
# 내장함수 min(), max(), sum(), len() 활용
