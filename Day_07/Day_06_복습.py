# 홀수 짝수 확인

# A = int(input("숫자를 하나 말씀해주세요! 제가 홀수인지 짝수인지 알려드릴게요! : "))
# B = A % 2
# if B == 0 or A == 0:
#     print("짝수입니다!")
# else:
#     print("홀수입니다!")

# 알파벳 탐지기

# alpha = str(input("안녕하세요, 문자 한 개를 입력해주세요! 만약 알파벳이라면 '알파벳입니다!'를, 그렇지 않다면 '알파벳이 아니에요'라고 알려드릴게요! : "))
# if alpha.isalpha():
#     print("알파벳입니다!")
# else:
#     print("알파벳이 아니에요")

# 비밀번호 설정 프로그램

# password = input("비밀번호 작성 : ")
#
# if len(password) <= 10:
#     print("최소 10글자 이상 설정하세요!")
# elif password.isalnum() or ('!' in password or '@' in password or '#' in password)
#     print("영어와 숫자를 꼭 포함해 주세요!")
# else:
#     if not ('!' in password or '@' in password or '#' in password):
#         print("특수문자를 !@# 포함해주세요!")
#     else:
#         print("비밀번호 설정 완료!")

# 버스 요금 계산기
# 사용자로부터 버스 노선의 종류를 나타내는 정수와 승객의 나이를 입력받습니다.

bus = {
    1: {
        'name': '시내버스',
        'price': 1200,
    },
    2: {
        'name': '광역버스',
        'price': 2000,
    },
    3: {
        'name': '마을버스',
        'price': 1000,
    },
}
bus_choice = int(input(f'버스를 선택하세요 1.시내버스 - 1200원, 2.광역버스 - 2000원, 3.마을버스 - 1000원')) - 1
age = int(input("나이를 입력하세요 : "))

if age <= 7 or 65 <= age:
    print("무료입니다")
elif 8 <= age and age <= 19:
    print(f"{bus[bus_choice]['name']}의 {bus[bus_choice]['price']*0.7}가격 입니다.")
else:
    print(f"{bus[bus_choice]['name']}의 {bus[bus_choice]['price']}가격 입니다.")





