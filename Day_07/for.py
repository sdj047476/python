# for - 2

# for x in range(10):
#     print(x)
# print("End")

# num = int(input("몇번까지 보실? "))+1
# for x in range(num):
#     if x % 2 == 0:
#         print(x)
# print("End")



# 유저한테 정수 입력 받. 그 수의 배수

# A = int(input("Number(1~100) : "))
#
# for x in range(1001):
#     if x != 0 and (A * x) <= 1000:
#         print(f"{A * x}")



# 1부터 10까지의 총합

# N = int(input("정수 입력: "))
# Sum = 0
# for x in range(N + 1):
#     Sum += x
# print(Sum)


# 유저에게 n의 정수를 받고, m의 정수를 받으면
#  0~n 까지의 m의 배수의 총합을 나타내는 프로그램
#
# n = int(input("0~n 까지의 m의 배수의 총합을 나타내는 프로그램 n 입력 : "))
# m = int(input("0~n 까지의 m의 배수의 총합을 나타내는 프로그램 m 입력 : "))
# Sum = 0
# for x in range(n+1):
#     if x % m == 0:
#         Sum += (x)
#
# print(Sum)

# random, list, for 활용 0부터 10000까지의 아무 숫자까지 수중 랜덤한 6개의 수 리스트 출력.
Nlist = []
for x in range (5):
    import random
    N = input(random.randint(0,10000))
    Nlist.append(N)
print(Nlist)




