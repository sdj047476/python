#list_advance - 1

# + 연산자

coffee = ['아메리카노','라떼','바닐라라떼']
cookie = ['초코 쿠키','녹차 쿠키','오레오 쿠키']
menu = coffee + cookie
print(menu)

# * 연산자
# * : int * int (사칙연산)
# * : str * str (str을 n번 반복)
# * : list * list (list를 n번 반복)

double_menu = menu * 2
print(double_menu)

# in 연산자 - boolean 타입 변환

print('라떼' in menu)

# [:] 슬라이싱 연산자

NewMenu = menu[1:4]
print(NewMenu)



# 리스트 기능
# 1. 리스트의 길이 기능 : len()
store = ['CU','GS','SevenEleven','Ministop']
print(len(store)) #4

# 2. 리스트 추가 : append()
store.append('Emart24')
print(store)

# 3. 리스트 추가[몇번째 추가] : insert( , )
store.insert(1,'Familymart')
print(store)

# 4. 리스트 제거 : remove()
store.remove('CU')
print(store)

# 5. 리스트 해당 아이템 위치 찾기 : index()
print(store.index('Ministop'))

# 6. 리스트에 해당 아이템 몇개인지 세기 : count()
print(store.count('Emart24'))

# 7. 리스트를 추가 : extend() '+'와 같은 역할
newStore =  ['Storyway','Buytheway']
store.extend(newStore)
print(store)

# 8. 리스트 정렬 : sort() / sort(Reverse=True)
store.sort()
print(store)
store.sort(reverse=True) #역으로 정렬
print(store)