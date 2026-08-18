# value counts 기본 코드

import pandas as pd

df = pd.read_csv('data/14_hydraulic.csv', encoding='utf-8')
df.info()
print(df.head(3))

df_old = df[ df['냉각기상태'] == '고장' ]
print(len(df_old)) # 40
# 하지만 이 방식으로 모든 상태를 일일이 찾아서 통계내는 것은 비효율적
# '고장'외에도 모든 경우를 한번에 모아서 경우마다의 나타나는 갯수를 찾기
# value_counts

# 냉각기상태별 사이클 건수 세기
print(df['냉각기상태'].value_counts())
# 냉각기상태
# 고장    40
# 저하    40
# 정상    40

# results 컬럼의 정상/고장 건수 세기
print(df['result'].value_counts())
# result
# 정상    67
# 고장    53

# 케이스마다 갯수 말고 비율로 알아보기
# 정규화 (normalize)
print(df['result'].value_counts(normalize = True))
# result
# 정상    0.558333
# 고장    0.441667

# 정규화 비율 결과를 위와 같이 쓰기보다는 round 처리로 반올림 할때가 많다
print(df['result'].value_counts(normalize = True).round(3))
# result
# 정상    0.558
# 고장    0.442
