# while - 2
# 조건식이 특정 탈출 경우가 없으면 무한 루프에 빠진다

#####################################################
# while문 첫번째 사용법
# a = 1
# while a < 10:
#     print('americano') # 무한루프에 빠짐
#     a += 1

#######################################################
# while문 두번째 사용법

# while True:
#     print("너가 숫자 1을 넣어야 탈출 가능")
#     num = int(input("숫자 입력 : "))
#     if num == 1:
#         break

##########################################################


# while : 유저가 끝을 결정
# for : 프로그래머가 끝을 결정 짓는 상황

##########################################################

#커피

coffeeList = [] # 데이터베이스, 엑셀 가져오는 데이터 코드
while True:
    print("메가커피 프로그램\n1.커피 등록하기\n2.커피 메뉴보기\n3.시스템 종료")
    codeNumber = int(input("번호 입력: "))
    if codeNumber == 1:
        print("커피 등록 시스템")
        coffeeName = input("커피 이름 입력: ")
        coffeeList.append(coffeeName)
        print("등록 완료!")
    elif codeNumber == 2:
        if len(coffeeList) == 0:
            print("커피 메뉴가 없습니다\n 커피 메뉴를 등록해주세요")
        else:
            print(coffeeList)
    elif codeNumber == 3:
        print("이용해 주셔서 감사합니다")
        break
    else:
        print("숫자를 제대로 입력해주세요")


