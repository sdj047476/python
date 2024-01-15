# for_comp - 3
# for문의 심화/축약 버전

# a = [i for i in range(101)]
# b = [i for i in range(1, 501)]
# c = [i for i in "megastudy"]
# print(a)
# print(b)
# print(c)

# d = [i*2 for i in range(1, 101)]
# print(d)

##################################################################

# 1. 1~10을 각각 제곱한 수의 리스트

# e = [i ** 2 for i in range(1, 11)]
# print(e)

# 2. 1~10에 각각 5를 더한 수의 리스트

# f = [i + 5 for i in range (1, 11)]
# print(f)

##################################################################

# for comprehension 조건문
# 1. if가 뒤에 있을 때는 filter 역할
# g = [i for i in range(1, 101) if i % 5 == 0]
# fruits = ['apple', 'strawberry', 'mango', 'orange', 'melon']
# h = [i for i in fruits if i.count('a') > 0] # 'a' 하나 이상 포함
# i = [i for i in fruits if i.count('r') == 1] # 'r'이 하나만 포함
# j = [i for i in fruits if len(i) >= 6] # 6글자 이상인 단어들만 포함

# 2. if - else 있을 때는 변환/치환 역할

# k = ['🍓' if i % 2 == 0 else i for i in range(1, 101)]

# 1. 유저에게 n을 입력 받고, 1~100까지 리스트를 출력을 하는데,
# n의 배수만 '🥕'을 표현해주고 나머지는 숫자로 표현

# l = int(input("정수 l 입력 : "))
# m = [l * i for i in range(1, 51) if l * i <= 100]

# 2. fruits = ['apple', 'strawberry', 'mango', 'orange', 'melon']
# fruits에서 5글자 이하면 대문자로 바꿔서 출력하고
# 아니면 🐇로 출력하는 리스트 만들기

# fruits = ['apple', 'strawberry', 'mango', 'orange', 'melon']
# n = [i.upper() if len(i) <= 5 else '🐇' for i in fruits]

######################################################################

# for 컴프리헨션 중첩 루프문
# o = [i * j for i in range(1, 4) for j in range(1, 4)]
# p = [i + j for i in ["apple", "banana"] for j in ["pie", "tanghuru"]]