#if - 2

# 조건문 - if

# num = int(input("정수 입력:"))
#
# if num > 0:
#     print("양의 정수 입니다.")
# elif num == 0:
#     print("0 입니다")     #elif 반복 가능
# else:
#     print("음의 정수 입니다.")









#유저에게 영어 점수를 입력받고
#100~90 'A입니다'
#90~80 'B입니다'
#80~70 'C입니다'
#70 미만 '재수강입니다'

# EnglishScore = int(input("영어 점수 입력 : "))
# if EnglishScore >= 90:
#     print("A")
# elif EnglishScore >= 80:
#     print("B")
# elif EnglishScore >= 70:
#     print("C")
# else:
#     print("F")
#
# a = 10
# if a > 0:
#     if a < 20:
#         print('a는 20보다 작은 양의 정수 입니다.')
#     else:
#         print('a는 20보다 큰 양의 정수 입니다.')
# else:
#     if a == 0:
#         print('a는 0입니다.')
#     else a < 0:
#         print('a는 음수입니다.')


#유저에게 정수를 입력받고
# 양의 홀수, 양의 짝수, 0, 음의 홀수, 음의 짝수

# Num = int(input("정수 입력 : "))
# Num_2 = Num % 2
# if Num > 0:
#     if Num_2 == 0:
#         print("양의 짝수")
#     else:
#         print("양의 홀수")
# elif Num < 0:
#     if Num_2 == 0:
#         print("음의 짝수")
#     else:
#         print("음의 홀수")
# else:
#     print("0")





#유저에게 비밀번호 설정을 입력받고
#만약에 8글자 보다 작으면 비밀번호가 8글자 이하입니다!
# 만약에 비밀번호에 !없으면 특수문자가 없습니다.
# 다 통과 된다면 비밀번호 완료!


passWord = list(input("설정할 비밀번호 입력 : "))
if len(passWord) < 8:
    print("비밀번호가 8글자 이하입니다.")
elif ('!') not in passWord:
    print("특수문자 !가 없습니다.")
else:
    print("비밀번호 설정 완료!")







