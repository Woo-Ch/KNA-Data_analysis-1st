# 실습1. finally로 파일 안전하게 닫기

# 1단계. try 블록에서 파일을 열어 처리
# 2단계. 처리 도중 오류가 날 수 있음을 가정
# 3단계. finally 블록에 close를 넣어 오류 여부와 상관없이 닫기
# 4단계. 일부러 오류를 내도 finally가 실행되는지 확인


try:
    f = open("sample.txt", "r", encoding="utf-8")

    print(f.read())
    result = 10 / 0
finally:
    f.close()
    print("파일을 닫았습니다.")

# result = 10 / 0 때문에 ZeroDivisionError가 남에도 불구하고
# finally의 f.close()가 정상적으로 작동된 후
# 오류가 발생함.
# 따라서 finally가 실행되는 것 확인 완료!!
