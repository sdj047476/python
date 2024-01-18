# map_filter - 3
# map (어떻게, 무엇을) - 변경/치환해주는 함수

numList = [1, 2, 3, 4, 5]
coffeePriceList = [2000, 3000, 3500, 4000]
fruits = ['apple', 'banana', 'mango', 'avocado']
a = map(lambda x: x ** 2, numList)
b = map(lambda x: x + 100, numList)
c = map(lambda x: x ** 2 + 100, numList)
d = map(lambda x: str(x + 1000) + '원', coffeePriceList)
e = map(lambda x: len(x), fruits)
print(list(a))
print(list(b))
print(list(c))
print(list(d))
print(list(e))

########################################################################

# filter (어떻게, 무엇을) 컷/필터

numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fruits = ['apple', 'banana', 'mango', 'avocado']
f = filter(lambda x: x > 5, numList)
g = filter(lambda x: x % 2 == 0, numList)
h = filter(lambda x: 'o' in x, fruits)
i = map(lambda x: '😽 ' + str(x), filter(lambda x: len(x) >= 6, fruits))
print(list(f))
print(list(g))
print(list(h))
print(list(i))
