# 영어로 표기되어있는 숫자를 수로 바꾸려고 합니다. 문자열 numbers가 매개 변수로 주어질 때
# numbers를 정수로 바꿔 return 하도록 solution 함수를 완성해 주세요.
# "one" -> "1"

def solution(numbers):
    numList = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for index, item in enumerate(numList):
        numbers = numbers.replace(item, str(index))
    return numbers

a = solution("zeroonezerofiveninezerofivezerosixseveneight")
print(a)