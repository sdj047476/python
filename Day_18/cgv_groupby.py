# cgv_groupby - 2
import pandas as pd

df = pd.read_csv('cgv.csv')

# # 데이터 프레임의 멤버 변수
# # 행과 열의 수
# print(df.shape)
# # 행 정보
# print(df.index)
# # 열 정보
# print(df.columns)
# # 데이터
# print(df.values)
#
# # 데이터 프레임의 멤버 함수
# # 위에서 20개 가져오기
# print(df.head(20))
# # 뒤에서 20개 가져오기
# print(df.tail(20))
# # 전체 데이터 요약본
# print(df.describe())

#######################################################

# # group_by : 기준 잡기
# # 영화 별로 그룹핑
# group_by_movies = df.groupby('movies')
# ages_group_by_movies = group_by_movies['ages'].value_counts()
# print(ages_group_by_movies)

# group_by_times = df.groupby('times')
# drinks_group_by_times = group_by_times['drinks'].value_counts()
# print(drinks_group_by_times)

# # 나이대 별로 지불 그룹핑
# group_by_age = df.groupby('ages')
# payments_group_by_age = group_by_age['payments'].value_counts()
# print(payments_group_by_age)

# # 영화 별로 스낵 그룹핑
# group_by_movies = df.groupby('movies')
# snacks_group_by_movies = group_by_movies['snacks'].value_counts()
# print(snacks_group_by_movies)

# # 시간대 별로 영화 그룹핑
# group_by_times = df.groupby('times')
# movies_group_by_times = group_by_times['movies'].value_counts()
# print(movies_group_by_times)

# # 시간대 별로 가장 인기 있는 영화
# popular_movies = df.groupby('times')['movies'].value_counts().groupby(level=0).head(1)
# print(popular_movies)
# # 함수화
# def most_x_to_y(x, y):
#     return df.groupby(x)[y].value_counts().groupby(level=0).head(1)
# print(most_x_to_y('ages', 'snacks'))
# print(most_x_to_y('times', 'payments'))
