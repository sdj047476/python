# for_1 - 1

# sum = 0
# for x in range(10):
#     if x % 2 == 0:
#         sum += x

##################################################

# 유저에게 대문자와 소문자가 섞인 문자를 받았을때, 반대로 출력하는 프로그램 inPuT -> INpUt

# W = input("대문자와 소문자가 섞인 영어 단어 : ")
# word = ''
# for i in W:
#     if i.isupper():
#         word += i.lower()
#     else:
#         word += i.upper()
# print(word)

#################################################

# A랑 E가 빠지는 프로그램

# A = input("영단어 쓰기 : ")
# word = ''
#
# # for i in A:
# #     if i == 'a' or i == 'e' or i == 'A' or i == 'E':
# #        pass # 의미없는 코드 넘기기
# #     else:
# #         word += i
#
# # 모음 빼기
# for i in A:
#     if i in 'aeiou':
#        pass # 의미없는 코드 넘기기
#     else:
#         word += i
#
# print(word)

####################################################

# list = []
# for x in ['사과', '바나나', '파인애플']:
#     list.append(len(x))
# print(list)

####################################################

# 홀수만 리스트, 짝수의 총합
# list = []
# sum = 0
# for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     if x % 2 == 0:
#        sum += x
#     else:
#        list.append(x)
# print(f"홀수 리스트 : {list} 짝수의 총합 : {sum}")

######################################################

# 0~10000를 담은 100개의 정수의 리스트
# 출력
# 이 리스트에서 홀수이면 '🥕' 짝수면 '🐇'

# import random
#
# num = []
# num_2 = []
# for x in range(100):
#     num.append(random.randint(0, 10001))
# num.sort()
# for i in num:
#     if i % 2 == 1:
#         num_2.append("🥕")
#     else:
#         num_2.append("🐇")
#
# print(num)
# print(num_2)

##########################################################

fruits = ["사과", "바나나", "체리"]
for index, fruit in enumerate(fruits):
	print(index, fruit)

