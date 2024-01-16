# dict_comp - 1
# normal_popcorn = {
#         'name': '일반 팝콘',
#         'price': '2500',
# }

#####################################################################

# coffee = ['americano', 'latte', 'vanilla']
# price = [2500, 3000, 3500]
# caffeine = [120, 150, 50]
# zipper
# zipped = zip(coffee, price)
# print(list(zipped)) # [('americano', 2500), ('latte', 3000), ('vanilla', 3500)]
#
# result = [{'메뉴': x, '가격': y} for x, y in zip(coffee, price)]
# print(result) # [{'메뉴': 'americano', '가격': 2500}, {'메뉴': 'latte', '가격': 3000}, {'메뉴': 'vanilla', '가격': 3500}]
#
# result_2 = [{'메뉴': x, '가격': y, '카페인': z} for x, y, z in zip(coffee,price,caffeine)]
# print(result_2)

############################################################################

# coffee = ['아메리카노', '라떼', '바닐라']
# price = [2500, 3000, 3500]
#
# a = {index:{'이름': coffee, '가격': price} for index, (coffee, price) in enumerate(zip(coffee,price))}
# # 몇번째인지 확인하고 싶으면 enumerate 사용
# print(a)
# for index, item in enumerate(coffee):







