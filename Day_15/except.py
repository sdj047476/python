# except - 1

try: # try는 에러가 날것 같은 구문을 적는곳
    num = int(input("숫자 입력. "))
    result = 10 / num
    print(f"결과는 {result}")
except Exception:
    print("Error.")
else:
    print("에러 없습니다.")
finally:
    print("에러 나도 상관 없으니 일단 보여주라")
