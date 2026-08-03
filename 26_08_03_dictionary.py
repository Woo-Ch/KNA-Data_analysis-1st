# 리스트로 크루 여러분의 이름을 나열해봅시다
data_class = ["태구", "수진", "영준"]

# 딕셔너리로 정확하게 역할까지 부여해봅시다
data_class_dict = {
    "반장": "태구",
    "부반장": "수진",
    "당번": "영준",
}

# 센서로 부터 얻는 예시 데이터로 딕셔너리를 만들어봅시다
sensors = {"센서이름": "보일러", "모터온도": 78, "진동": 0.5}

print(sensors)
print(type(sensors))  # <class 'dict'>
empty = {}
print(type(empty))  # <class 'dict'>

print(sensors["모터온도"])  # 78
print(sensors["센서이름"])  # 보일러
print(sensors["진동"])  # 0.5

# 기존에 있던 key의 값을 변경
sensors["센서이름"] = "펌프"  # 센서이름 값 변경

print(sensors["센서이름"])  # 펌프

# 기존에 없던 key의 값을 추가
sensors["펌프입력"] = 95
sensors["유량"] = 42

print(sensors["펌프입력"])  # 95
print(sensors)
# {'센서이름': '펌프', '모터온도': 78, '진동': 0.5, '펌프입력': 95, '유량': 42}

# 더 이상 필요없는 key와 그 value를 삭제
del sensors["펌프입력"]
del sensors["유량"]

print(sensors)  # {'센서이름': '펌프', '모터온도': 78, '진동': 0.5}

# 더 이상 없는 key를 호출하면 에러 발생
# print(sensors["펌프입력"])  # KeyError: '펌프입력'

# .get()은 딕셔너리에서 값을 안전하게 꺼내는 함수
print(sensors.get("센서이름"))  # 펌프
print(sensors.get("펌프입력"))  # None

motor_degree = sensors.get("모터온도")
next_degree = motor_degree + 10
print(next_degree)  # 88

is_motor_degree_key = "모터온도" in sensors
print(is_motor_degree_key)  # True

if is_motor_degree_key:
    print("모터온도 키가 존재합니다.")
else:
    print("모터온도 키가 존재하지 않습니다.")

# 위 코드는 이렇게 보통 쓰인다.
if "모터온도" in sensors:
    print("모터온도 키가 존재합니다.")
else:
    print("모터온도 키가 존재하지 않습니다.")

# keys를 가져와봅시다.
print(sensors.keys())  # dict_keys(['센서이름', '모터온도', '진동'])
# values를 가져와봅시다.
print(sensors.values())  # dict_values(['펌프', 78, 0.5])
# len를 통해 몇개의 key-value 조합들이 있는지 살펴봅시다.
print(len(sensors))  # 3

for key, value in sensors.items():
    print(key)
    print(value)

# 위와같이 사용하기 보다는, 의미있는 이름으로 사용한다
for name, value in sensors.items():
    print(name)
    print(value)

if len(sensors) <= 5:
    print("센서가 5개 이하입니다.")

# 재미난 사례를 추가로 만들어봅시다
# 나라 이름들로 정리해봅시다
# 유럽 : 스페인(ESP), 프랑스(FRA), 독일(DEU), 스위스(SUI), 네덜란드(NLD)
# 아시아: 한국(KOR), 일본(JPN), 중국(CHN), 사우디(SAU), 이란(IRN)
# 남미: 아르헨티나(ARG), 브라질(BRA), 칠레(CHI), 콜롬비아(COL), 우루과이(URU)
# 각 나라마다 이름과 약칭으로 정리 가능합니다

korea = {"국가명": "대한민국", "약칭": "KOR"}
japan = {"국가명": "일본", "약칭": "JPN"}

# 아시아 나라들을 하나의 리스트로 모아봅시다
asia = [korea, japan]
print(asia)
# [{'국가명': '대한민국', '약칭': 'KOR'}, {'국가명': '일본', '약칭': 'JPN'}]

# 유럽 나라들을 하나의 리스트로 모아봅시다
europe = [
    {"국가명": "스페인", "약칭": "ESP"},
    {"국가명": "프랑스", "약칭": "FRA"},
    {"국가명": "독일", "약칭": "DEU"},
    {"국가명": "스위스", "약칭": "SUI"},
    {"국가명": "네덜란드", "약칭": "NLD"},
]
print(europe)

for country in europe:
    print(country.get("국가명", "없음"))

    for key, value in country.items():
        print(key, value)

# 여러분의 조별과제
# 포켓몬 1, 2, 3 진화단계들을 딕셔너리로 만들고
# 그 포켓몬 딕셔너리들이 최소 10개 모인 배열을 만들어봅시다.
# 그 배열 데이터를 화면에 print 합니다
# 가능하면 그 배열의 데이터들을 for-in을 사용해서 하나씩 꺼내 print 합시다(선택)

pokemon_list = [
    {"포켓몬": "구구", "2단계": "피죤", "3단계": "피죤투"},
    {"포켓몬": "이상해씨", "2단계": "이상해풀", "3단계": "이상해꽃"},
    {"포켓몬": "고오스", "2단계": "고우스트", "3단계": "팬텀"},
    {"포켓몬": "물짱이", "2단계": "수륙챙이", "3단계": "강챙이"},
    {"포켓몬": "파이리", "2단계": "리자드", "3단계": "리자몽"},
    {"포켓몬": "미뇽", "2단계": "신뇽", "3단계": "망나뇽"},
    {"포켓몬": "캐터피", "2단계": "단데기", "3단계": "버터플"},
    {"포켓몬": "꼬부기", "2단계": "어니부기", "3단계": "거북왕"},
    {"포켓몬": "삐삐", "2단계": "픽시", "3단계": "메가픽시"},
    {"포켓몬": "또가스", "2단계": "또도가스", "3단계": "또또도가스"},
]

for pokemon in pokemon_list:
    print(pokemon.get("포켓몬"))

    for key, value in pokemon.items():
        print(key, value)

# 두 딕셔너리를 key-value 조합으로 하나씩 꺼내어 비교하기
# 다음의 두 딕셔너리는 같은 key들을 가지고 있습니다.
# 실제 데이터
values = {"모터온도": 95, "압력": 88}
# 임계치 데이터
limits = {"모터온도": 90, "압력": 90}

for name, value in values.items():
    print(f"{name}: {value}")

    # limits 딕셔너리에도 name의 key가 있다면, 가져와서 비교하자!
    if value > limits.get(name, 0):
        print(name, "경고")


sensors = {"모터온도": 78, "진동": 0.5}
new_data = {"모터온도": 80, "유량": 42}
sensors.update(new_data)  # 기존 딕셔너리에 새로운 딕셔너리의 key-value 조합을 추가
print(sensors)  # {'모터온도': 80, '진동': 0.5, '유량': 42}


# zip으로 key들의 배열과 value들의 배열을 묶어서 새로운 딕셔너리를 만들 수 있다
names = ["모터온도", "진동", "압력"]
values = [78, 0.5, 95]
sensors = dict(
    zip(names, values)
)  # zip기능으로 두 배열을 사용해 묶고 dict 타입 딕셔너리로 만들기
print(sensors)  # {'모터온도': 78, '진동': 0.5, '압력': 95}

# 딕셔너리 안에 value로 리스트도 가능합니다.
my_classroom = ({"학년": 3, "반": 1, "반장": "홍길동", "부반장": ["고길동", "둘리"]},)
{"학년": 3, "반": 2, "반장": "메타몽", "부반장": ["고라파덕", "피카츄"]}


# 딕셔너리 안에 value로 딕셔너리를 사용하기
kbo = [
    {
        "구단명": "삼성",
        "마스코트": "라이온스",
        "구장": {"1구장": "대구라이온스파크", "2구장": "포항야구장"},
    },
    {
        "구단명": "두산",
        "마스코트": "베어스",
        "구장": {"1구장": "잠실야구장", "2구장": "베어스파크"},
    },
]

# 쉽게 배열 안에 딕셔너리 안에 딕셔너리 접근하기
print(kbo[0]["마스코트"])  # 라이온스
print(kbo[0]["구장"])  # {'1구장': '대구라이온스파크', '2구장': '포항야구장'}
print(kbo[0]["구장"]["1구장"]) # 대구라이온스파크


