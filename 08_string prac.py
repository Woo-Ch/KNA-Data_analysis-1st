# 실습. 설비 정보 출력 카드 만들기

# 출력 결과물
# 설비: PUMP_A
# 상태: 정상
# 가동: 1200
# 점검: 2026-07-16
#
# 삼중따옴표 금지, 이스케이프 문자 사용
# 변수 지정하기
# 가동은 int로 저장

machine = "PUMP_A"
status = "정상"
operate = 1200
inspection = "2026-07-16"

card = "설비: " + machine + "\n상태: " + status + "\n가동: " + str(operate) + "\n점검: " + inspection
print(card)

