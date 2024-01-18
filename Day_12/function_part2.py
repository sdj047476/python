# function_part2 - 1

# 가변 매개 변수


# def makePizza(*toppings):
#     print("다음 피자는 아래의 토핑이 들어갑니다.")
#     for i in toppings:
#         print(i)
# makePizza("pineapple")
# makePizza("pineapple", "cheese")
# makePizza("pineapple", "cheese", "mushroom")

######################################################################

# [자(쥐), 축(소), 인(호랑이), 묘(토끼), 진(용), 사(뱀), 오(말), 미()양, 신(원숭이), 유(닭), 술(개), 해(돼지)]
def zodiac(*years):
    sign = ['닭', '개', '돼지', '쥐', '소', '호랑이', '토끼', '용', '뱀', '말', '양', '원숭이']
    # newList = []
    # for i in years:
    #     newList.append(sign[i - 1993])
    # return newList
    return [sign[i - 1993] for i in years]

a = zodiac(1993, 2002, 2003, 2004)
print(a)
