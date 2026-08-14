# 실습 4. 부정·목록·범위 조건
# 부정·목록 매칭·범위 조건을 각각 적용
import pandas as pd

df = pd.read_csv("data/13_diecasting_shot.csv")
df.info()

# · 물결 기호로 고장이 아닌 설비만 뒤집어 추출
print(df.tail())  # 품질등급 컬럼에 불량 항목 발견!
print(df[df["품질등급"] == "불량"].head())  # 추려본 내용에 '불량'만 모인듯
print(len(df[df["품질등급"] == "불량"]))  # 20

# 그렇다면 '불량' 아닌것들은?
print(df[~(df["품질등급"] == "불량")].head())  # '불량 없는듯
print(len(df[~(df["품질등급"] == "불량")]))  # 180

# · isin으로 품질등급이 특정 목록에 속하는 행 추출 - 품질등급 - 양품 또는 주의
print(df[(df["품질등급"] == "양품") | (df["품질등급"] == "주의")].head())
print(len(df[(df["품질등급"] == "양품") | (df["품질등급"] == "주의")]))  # 180

print(df[df["품질등급"].isin(["양품", "주의"])].head())
print(len(df[df["품질등급"].isin(["양품", "주의"])]))  # 180

# · between으로 실린더압력가 지정 범위에 든 행 추출 : 210~230
print(df[df["실린더압력"].between(210, 230)].head())
print(len(df[df["실린더압력"].between(210, 230)]))  # 89

# 그 외의 것들이 200 - 89 = 111개 나오는지 확인하기
print(len(df[~(df["실린더압력"].between(210, 230))]))  # 111

# 예상 결과
# 순서대로 192건·94건·108건 출력 x
