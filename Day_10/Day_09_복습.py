# 1. 리스트 컴프리헨션을 이용한 짝수 생성

print("리스트 컴프리헨션을 이용한 짝수 생성")
a = [i for i in range(1, 21) if i % 2 == 0]
# [i for i in range(2, 21, 2)]
print(a)

# 2. 조건을 포함한 리스트 컴프리헨션

print("조건을 포함한 리스트 컴프리헨션")
b = [i for i in range(1, 11)]
c = [i for i in b if i > 5]
print(c)

# 3. 문자열 처리를 위한 리스트 컴프리헨션

print("문자열 처리를 위한 리스트 컴프리헨션")
List = ['apple', 'banana', 'cherry', 'date']
d = [i[0] for i in List]
print(d)

# 4. List를 대문자화

print("List를 대문자화")
e = [i.upper() for i in List]
print(e)
