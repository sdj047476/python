# cgv_pie - 4
# 일변량 그래프
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('cgv.csv')

# snacks_by_times = df.groupby('times')['snacks'].value_counts()
# normal_time_snack = snacks_by_times['일반']
#
# plt.rcParams['font.family'] = 'Malgun Gothic' # 폰트 설정
# normal_time_snack.plot.pie(autopct='%1.1f%%') # plot.pie() 파이그래프, autopact = 소수점자리
# plt.show()

drinks_by_movies = df.groupby('movies')['drinks'].value_counts()
movie_drinks = drinks_by_movies['웡카']

plt.rcParams['font.family'] = 'Malgun Gothic'
movie_drinks.plot.pie(autopct='%1.1f%%') # plot.pie() 파이그래프, autopact = 소수점자리
plt.show()
