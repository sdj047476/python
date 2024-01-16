# function - 2
# # 함수: 코드를 모아놓은 묶음
#
# # 파이썬 내장 함수
# # print(), input(), int() ...
#
# # 파이썬 커스터마이즈 함수
# def add(x, y):
#     result = x + y
#     return result
#
# a = add(5, 10)
# print(a)
#
# # minus 함수
#
# def minus(x, y):
#     result = x - y
#     return result
#
# # multiply 함수
#
# def multi(x, y):
#     result = x * y
#     return result
#
# # 숫자 홀,짝 판별 함수
#
# def num(x):
#     if x % 2 == 0:
#         return "짝수입니다."
#     else:
#         return "홀수입니다."
#
# # Dic화
# def makeListDict(xList, yList, xKey, yKey):
#     return [{xKey: x, yKey: y} for x, y in zip(xList, yList)]
#
breads = ['소금빵', '보름달', '단팥빵', '앙버터', '마카롱']
price = [2500, 1000, 2400, 4500, 3000]
# result = makeListDict(breads, price, '빵', '가격')
# print(result)

#
def makeListDict(xList, yList, xKey = 'item', yKey = 'price'):
    return [{xKey: x, yKey: y} for x, y in zip(xList, yList)]

result = makeListDict(xList = breads, yList = price)
print(result)