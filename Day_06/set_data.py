#set_data - 1

megastudy = {
    'python': [1,2,3],
    'java': [1,3,5],
    'clang': [2,4,6]
}

# python의 날짜 가져오기
# 1. megastudy['python'] _연산자
# 2. megastudy.get('python') _기능
# megastudy.get('javascript', '수업없음') #javascript가 있으면 가져오고, 없으면 '수업없음'으로 대체됨
# print(list(megastudy.keys())) #['python', 'java', 'clang']
# print(list(megastudy.values())) #[[1, 2, 3], [1, 3, 5], [2, 4, 6]]
# print(list(megastudy.items())) #[('python', [1, 2, 3]), ('java', [1, 3, 5]), ('clang', [2, 4, 6])]



#set (집합) 중복 안됨
a = {1,2,3,1,2,3,1,2,3}
b = set([1,2,3,4,1,2,3,])
b.add(1)
b.add(5)
b.discard(3) #3만 없애기
b.clear() #싹다 없애기
print(b)
print(a)



