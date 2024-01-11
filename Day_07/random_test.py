#random_test - 1

import random


fruits =  ['apple','mango','banana','melon']

print(random.randint(0,100)) # 0~100 사이의 정수
print(random.random()) # 0~1 사이의 실수
print(random.choice(fruits))
random.shuffle(fruits)
print(fruits)