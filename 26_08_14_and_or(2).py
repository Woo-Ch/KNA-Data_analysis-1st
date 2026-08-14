import pandas as pd

# 기존에 우리가 알고있던 파이썬의 "그리고", "또는" 표시
a = 10
b = 5

if a > 5 and b < 3:
    print("이것이 '그리고'입니다")

if a > 5 or b < 3:
    print("이것이 '또는'입니다")

# 파이썬의 기본 and와 or은 양쪽 비교대상이 모두 Boolean이 되야한다.
# True/False외의 것은 비교대상이 안된다.

# 그렇다면 DF나 Serise에는 and/or로 처리불가? 불가!

df = pd.read_csv("data/13_diecasting_small.csv")
df.info()

df_sub1 = df[df["비스킷두께"] >= 13]
df_sub1.info()  # 6 entries

df_sub2 = df[df["사이클타임"] >= 25]
df_sub2.info()  # 6 entries

df_both = df[(df["비스킷두께"] >= 13) & (df["사이클타임"] >= 25)]
df_both.info()
print(len(df_both))  # 5

df_either = df[(df["비스킷두께"] >= 13) | (df["사이클타임"] >= 25)]
df_either.info()
print(len(df_either))  # 7
