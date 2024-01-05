
# 100미만의 정수를 입력받고 10의 자리와 1의 자리를 출력하는 프로그램

# Num = int(input("100 미만의 정수: "))
# print(f"10의 자리수: {Num // 10}, 1의 자리수: {Num % 10}")




# 1000이하 정수를 입력 받고 분과 초로 환산하는 프로그램

# Time = int(input("1000이하의 정수: "))
# Min = Time // 60
# Sec = Time % 60
# print(f"{Min}분 {Sec}초")


# 정수 10000~99999 사이 입력받고 100의 자릿값을 출력하는 프로그램

N =  int(input("10000~99999 정수 입력:"))
N_100 = N % 1000
print(f"100의 자릿수는 {N_100 // 100}")







## 비교 연산자 [결과:Bool]
# <, >, <=, >=, ==(같다), !=(다르다)
#print(3<1) #False

# a = 3 > 1 #a는 bool type
# b = 3 == 1 #b는 bool type [False]
# c = 3 != 1 #c는 bool type [True]





# ## 논리 연산자 [결과: bool]
# # and : 피연산자가 모두 Ture이면 True
# print(3 > 1 and 5 > 1) #True
# # or : 피연산자가 하나라도 True이면 True
# print(5 < 1 or 3 < 1 or 0 < 1) #True
# # not : False -> True, True -> False
# print(not(3 > 1)) #True -> False






## 할당 연산자
#a = 1 #1
# a = a + 3 #4

#a = 1 #1
#a += 3 #4

#a = 1 #1
#a -= 3 #-2

#a = 1 #1
#a *= 3 #3

# a = 1 #1
# a /= 3 #0.33333333333



