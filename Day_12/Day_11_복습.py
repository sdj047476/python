movie_names = ['액션 영화', '로맨틱 코미디', '다큐멘터리']
movie_prices = [12000, 10000, 11000]
popcorn_names = ['팝콘 세트', '스낵 콤보', '건강 팩']
popcorn_prices = [6000, 8000, 7000]
seat_names = ['일반 좌석', '프리미엄 좌석', 'VIP 좌석']
seat_prices = [0, 5000, 10000]


def create_dict(names, prices, key):
    return[{key: name, 'price': price} for name, price in zip(names, prices)]

