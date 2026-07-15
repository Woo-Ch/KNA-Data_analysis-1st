# print(NameError 만들기) # SyntaxError 발생 (띄어쓰기가 있어서 변수 2개를 쉼표 없이 작성했다고 추정)
# print(NameError만들기) # NameError 발생
# 코드는 위에서 아래로 실행하기 때문에 위에서 에러 발생 시 그 이후 코드 실행 X
print("NameError 만들기") # 따옴표로 감싸주면 에러 발생 X

# =========================================
print("=============SyntaxError 만들기===============")

# print("온도) # 따옴표를 안 닫음
# print("진동" # 괄호를 안 닫음

print("온도")
print("진동")

print("=============실습. 오류 하나씩 고치기===============")

# print(온도, 75)
# print("진동", 2.3
# print("압력": 4.0)

print("온도", 75) # NameError: 온도에 "" 처리가 안 되어 있음
print("진동", 2.3) # SyntaxError 끝에 )가 빠져 있음
print("압력:", 4.0) # SyntaxError :가 "" 처리가 안 되어 있음

