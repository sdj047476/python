# 1부터 100까지 사이의 수를 유저가 입력한 정수 n의 배수만 출력하도록 만드세요!


# num = int(input("1~100까지 사이의 수 입력: "))
#
# for i in range(101):
#     if i % num == 0 and i > 0:
#         print(i)





# 정수 n을 입력 받고, 구구단을 출력 해주세요

num1 = int(input("정수 입력:"))
for i in range(1,10):
    print(f"{num1} * {i} = {num1 * i}")
