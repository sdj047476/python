# break - 1
# break : for, while 의 반복을 끊는 역할
# continue : jump 와 같은 역할


for i in range(100):
    if i == 50:
        break
    elif i == 48:
        continue
    else:
        print(i)

