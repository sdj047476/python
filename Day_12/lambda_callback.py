# lambda_callback - 2
# 간결하고 이름이 없는 한 줄 함수

# plus = lambda a, b: a + b
# minus = lambda a, b: a - b
# multi = lambda a, b: a * b
#
# resultPlus = plus(5, 7)
# resultMinus = minus(5, 7)
# resultMulti = multi(5, 7)

# callback 함수
# something(add) -> 함수 안에 함수 (속 함수는 이름만... 호출은 안됨)

def hello(some):
    print("안녕")
    some()
def bye():
    print("잘가")

hello(bye)

#############################################################################

eggs = ['🥚''🥚''🥚']

def cookEggs(eggs, index, recipe):
    recipe(eggs, index)

def makefry(eggs, index):
    eggs[index] = '🍳'

def makeSandwich(eggs, index):
    eggs[index] = '🥪'

cookEggs(eggs,0,makefry)
cookEggs(eggs,1,makeSandwich)