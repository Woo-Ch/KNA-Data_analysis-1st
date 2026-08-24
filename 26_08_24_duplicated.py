import pandas as pd

df = pd.read_csv("data/16_diecasting.csv", encoding="utf-8")

print(df.duplicated())
# 0      False
# 1      False
# 2      False
# 3      False
# 4      False
#        ...
# 197    False
# 198    False
# 199    False
# 200     True
# 201     True
# Length: 202, dtype: bool

print(df[df.duplicated()])  # 완전 중복된 row들만 df로 추려내기
#  샷  실린더압력    주조압력  사이클타임  비스킷두께    형체력  상태
# 200   8  215.0  1038.0   20.9   11.0  258.0   0
# 201  89  235.0  1137.0   22.7   13.0  261.0   0
# 200번 행 → `0~199번 중 어딘가에 200번과 완전히 똑같은 행이 이미 있음
# 201번 행 → `0~200번 중 어딘가에 201번과 완전히 똑같은 행이 이미 있음
# duplicated()는 똑같은 데이터가 두 번 등장하면 뒤에 등장한 행을 True로 표시

# 중복된 원본까지 모두 보는 방법
print(df[df.duplicated(keep=False)])
# 샷  실린더압력    주조압력  사이클타임  비스킷두께    형체력  상태
# 7     8  215.0  1038.0   20.9   11.0  258.0   0
# 88   89  235.0  1137.0   22.7   13.0  261.0   0
# 200   8  215.0  1038.0   20.9   11.0  258.0   0
# 201  89  235.0  1137.0   22.7   13.0  261.0   0

print(df.duplicated(keep=False))
# 0      False
# 1      False
# 2      False
# 3      False
# 4      False
#        ...
# 197    False
# 198    False
# 199    False
# 200     True
# 201     True
# Length: 202, dtype: bool

# 중복 개수 확인하기
print(df.duplicated().sum())  # 2 / row들이 중복으로 더 존재함(먼저 확인 row 제외)
print(
    len(df)
)  # 202 : 전체가 202개 row로 2개 중복 빼면 순수하게 200개가 한줄씩 안겹치고 존재


# 중복 제거
# drop_duplicated(): 중복된 행들은 한 행만 남기고 깔끔하게 도려내는 함수입니다.
# subset=["샷"] 인자를 통해 특정 컬럼(예: 샷 번호 고유값)을 기준으로 유일성 검사 가능
# reset_index(drop=True): 중복을 지운 후 듬성듬성 깨져버린 원래의 일련번호 인덱스를 0부터
# 시작하는 촘촘한 정수로 새로 깔끔하게 정렬해 줍니다.
print(len(df.drop_duplicates()))  # 200

print(len(df.drop_duplicates().reset_index(drop=True)))  # 200

print(
    len(
        df.drop_duplicates(subset=["샷", "실린더압력", "주조압력"]).reset_index(
            drop=True
        )
    )
)
# 200

# 전체흐름
# 원본 df
#  ↓
# 샷 + 실린더압력 + 주조압력이 같은 행 제거
#  ↓
# 인덱스 다시 0, 1, 2...로 정리
#  ↓
# 남은 행 개수 세기
#  ↓
# 출력
