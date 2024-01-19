# 1. 문자열 뒤집기
# 문자열 my_string이 매개변수로 주어집니다. my_string을 거꾸로 뒤집은 문자열을 return하도록 함수

def reverseStr(my_string):
    strList = list(my_string)
    strList.reverse()
    word = ""
    for i in strList:
        word += i
    return word

# 2. 미완성된 할 일 찾기
# todo_list에 있는 할 일 중, finished 배열을 통해 아직 끝내지 못한 일들을 찾아 순서대로 배열에 담아 반환 하는 함수

todo_list = ["problem solving", "practice guitar", "swim", "study graph"]
finished = [True, False, True, False]

def haveto_List(todoList,finishedList):
    # newList = []
    # for index, item in enumerate(finishedList):
    #     if not item:
    #         newList.append(todoList[index])
    # return newList
    return [todoList[index] for index, item in enumerate(finishedList) if not item]

print(reverseStr("bread"))
print(haveto_List(todo_list, finished))
