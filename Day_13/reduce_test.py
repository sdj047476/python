# reduce_test - 1

# map (치환)
# filter (필터링)
# reduce (누적)

from functools import reduce # 이걸 써야 reduce 함수 사용가능

numbers = [1, 2, 3, 4, 5]

resultPlus = reduce(lambda x, y: x + y, numbers)
resultMulti = reduce(lambda x, y: x * y, numbers)

print(resultPlus)
print(resultMulti)