# pandas_101 - 4
# 엑셀을 파이썬화
# 판다스 데이터 타입: series, dataframe
# series: 엑셀에서 하나의 열
# dataframe: 엑셀 그 자체[스트페드 시트]

import pandas as pd
from faker import Faker

# numList = [12, 25, 65, 98, 9845]
# series = pd.Series(numList)
# print(series.mean())

###########################################################

coffeeData = {
    "menu": ['americano', 'latte', 'mocha', 'vanilla', 'mint'],
    "price": [2500, 3000, 3500, 3500, 4000],
    "caffein": [120, 100, 80, 100, 50]
}

# df = pd.DataFrame(coffeeData)
# print(df)
# df.to_csv('coffee.csv', index=False) # index=False 는 index 부분은 엑셀 파일로 옮기지 않게 한다.

fake = Faker('ko_KR')

carData = {
    "carName": ['K5', 'K7', 'AVANTE', 'K3', 'MODEL Y'],
    "owner": [fake.name() for i in range(5)],
}
# df = pd.DataFrame(carData)
# df.to_csv('car.csv', index=False)
