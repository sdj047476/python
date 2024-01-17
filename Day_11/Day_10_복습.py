# 1. 다음 리스트에서 길이가 5보다 크고, 문자'a'를 포함하는 문자열만
# 포함된 새로운 리스트를 생성하는 리스트 컴프리헨션을 작성하세요
import a as a

words = ["apple,", "banana", "cherry", "date", "elderberry", "fig"]
wordsWithA = [i for i in words if len(i) > 5 and 'a' in i]
print(wordsWithA)

# 2. 다음 리스트에서 50보다 큰 숫자만 포함된 새로운 리스트를 생성하는 리스트 컴프리헨션을 작성하세요.

numbers = [30, 55, 20, 75, 40, 90, 10, 65]
NumbersList = [i for i in numbers if i > 50]
print(NumbersList)

# 3. 두 정수 a,b와 boolean 변수 flag가 매개변수로 주어집니다.
# flag가 True이면 a + b를, False이면 a - b를 반환하는 PlusOrMinus 함수를 작성해주세요.

def PlusOrMinus (a, b, flag):
    if flag:
        return a + b
    else:
        return a - b


a = int(input("첫번째 정수 입력: "))
b = int(input("두번째 정수 입력: "))
flag = 0
print(PlusOrMinus(a, b, flag == 0))
