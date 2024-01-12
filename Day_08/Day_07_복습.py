
# 1. 각도 프로그램

# angle = int(input("각도 데이터 입력 요청. "))
#
# if 0 < angle < 90:
#     print("예각")
# elif angle == 90:
#     print("직각")
# elif 90 < angle < 180:
#     print("둔각")
# elif angle == 180:
#     print("평각")
# else:
#     print("오류. 프로그램 다시 실행후 1~180 사이의 정수 입력")

#############################################################

# 2. 테마파크 프로그램

# TP = {
#     1: {
#         'A': '일반 입장권',
#         'B': 50000,
#     },
#     2: {
#         'A': '프리미엄 입장권',
#         'B':  75000,
#     },
#     3: {
#         'A': 'VIP 입장권(모든 놀이기구 무제한 이용',
#         'B': 100000,
#     },
# }
# TP_A_user = int(input("테마파크 입장권 고르세요.\n\t1.일반 입장권\n\t2.프리미엄 입장권\n\t3.VIP 입장권\n번호 입력 : "))
# User_age = int(input("나이 입력 : "))
#
# if User_age < 12:
#     print(f"12살 미만은 50% 할인. 따라서 가격은 {int(int(TP[TP_A_user]['B']) / 2)}원.")
# elif User_age >= 65:
#     print(f"65세 이상은 30% 할인. 따라서 가격은 {int(int(TP[TP_A_user]['B']) * 0.7)}원.")
# else:
#     print(f"가격은 {TP[TP_A_user['B']]}원.")

#################################################################

#3. 난수 생성 및 리스트 표시 프로그램!???

import random

num = []
for i in range(6):
    num.append(random.randint(0,10001))
num.sort()
print(num)

