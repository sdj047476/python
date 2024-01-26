# cgv_data_maker - 1
import pandas as pd
import random
from faker import Faker
faker = Faker('ko_KR')

# name, ages, genders, movies, payments, snacks, drinks, times

ageList = [20, 30, 40, 50, 60]
agePercent = [30, 30, 20, 15, 5]
genderList = ['male', 'female']
movieList = ['웡카', '시민덕희', '도그맨', '너의 이름은', '외계인']
moviePercent = [40, 10, 5, 5, 40]
paymentsList = ['현금', '체크 카드', '신용 카드', '카카오 페이', '네이버 페이']
paymentsPercent = [5, 30, 35, 20, 10]
snacksList = ['선택 안함', '일반 팝콘', '카라멜 팝콘', '나쵸', '오징어', '맛밤']
snacksPercent = [40, 10, 20, 15, 10, 5]
drinksList = ['선택 안함', '콜라', '제로 콜라', '물', '에이드', '스프라이트', '오렌지 주스']
drinksPercent = [30, 10, 20, 10, 10, 15, 5]
timesList = ['조조', '일반', '심야']
timesPercent = [20, 70, 10]

data = {
    'name': [faker.name() for i in range(500)],
    'ages': [random.choices(ageList, weights=agePercent, k=1)[0] for i in range(500)],
    'genders': [genderList[random.randint(0, 1)] for i in range(500)],
    'movies': [random.choices(movieList, weights=moviePercent, k=1)[0] for i in range(500)],
    'payments': [random.choices(paymentsList, weights=paymentsPercent, k=1)[0] for i in range(500)],
    'snacks': [random.choices(snacksList, weights=snacksPercent, k=1)[0] for i in range(500)],
    'drinks': [random.choices(drinksList, weights=drinksPercent, k=1)[0] for i in range(500)],
    'times': [random.choices(timesList, weights=timesPercent, k=1)[0] for i in range(500)],
}

df = pd.DataFrame(data)
df.to_csv('cgv.csv', index=False)