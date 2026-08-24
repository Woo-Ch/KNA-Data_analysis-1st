import pandas as pd

df = pd.read_csv("data/16_diecasting.csv")

# 실습7. duplicated로 중복찾기와 개수
# 완전 중복 행을 찾고 keep 옵션으로 개수 비교

# 목표
# 완전 중복 행을 찾고 keep 옵션에 따른 개수 비교

# 단계
# · duplicated로 중복 행 여부를 참·거짓으로 표시
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

print(df[df.duplicated()])
# 샷  실린더압력    주조압력  사이클타임  비스킷두께    형체력  상태
# 200   8  215.0  1038.0   20.9   11.0  258.0   0
# 201  89  235.0  1137.0   22.7   13.0  261.0   0

# · sum으로 중복 개수 세고 중복 행 직접 확인
print(df.duplicated().sum())  # 2

# · keep을 거짓으로 두면 겹친 행이 모두 표시되는 것 확인
print(df[df.duplicated(keep=False)])
# 샷  실린더압력    주조압력  사이클타임  비스킷두께    형체력  상태
# 7     8  215.0  1038.0   20.9   11.0  258.0   0
# 88   89  235.0  1137.0   22.7   13.0  261.0   0
# 200   8  215.0  1038.0   20.9   11.0  258.0   0
# 201  89  235.0  1137.0   22.7   13.0  261.0   0

print(df.duplicated(keep=False).sum())  # 4

# 예상 결과
# 완전 중복 2건, keep을 끄면 겹친 행 4건 표시
