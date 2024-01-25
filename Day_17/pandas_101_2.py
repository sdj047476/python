import pandas as pd
from faker import Faker
faker = Faker('ko_KR')
import random

# print(faker.name())

coffeeList = ['americano', 'latte', 'vanilla', 'moca', 'mint']
# data = {'name': 30명, 'age':20~60 랜덤으로 30개, 'coffee': 30개}
data = {
    'name': [faker.name() for i in range(30)],
    'age': [random.randint(20, 60) for i in range(30)],
    'coffee': [random.choice(coffeeList) for i in range(30)],
}
df = pd.DataFrame(data)
print(df)
df.to_csv(f'dummy_data.csv', index=False)


