

#1.태어난 년도 입력받고 현재 만나이 출력

#userYear = int(input("몇년생이십니까:"))
#print(f"귀하의 나이는 만 {2023 - userYear}입니다.")

#Born_Year = int(input("태어난 년도:"))
#print(f"당신의 만나이는 : {2023 - Born_Year}")

#2.세개의 숫자 입력 받고 총합, 평균(실수) 출력

#FirstNum = float(input("첫번째 수:"))
#SecondNum = float(input("두번째 수:"))
#ThirdNum = float(input("세번째 수:"))
#sum = FirstNum + SecondNum + ThirdNum
#avg = sum/3
#print(f"세 수의 총합은 {FirstNum + SecondNum + ThirdNum}이고 평균은 {(FirstNum + SecondNum + ThirdNum)/3}입니다")
#print(f"총합: {sum}, 평균: {avg}")

#3.섭씨 온도를 입력받아 화씨 온도로 변환을 출력

C = float(input("현재 섭씨 온도는:"))
F = C * 5.9 + 32
#변수[실수]:.2f 둘째 자리까지 출력
print(f"오늘의 섭씨 온도는 {C}이고 화씨 온도는 {F:.2f}입니다.")

#4.사용자의 키(m)와 몸무게(kg)을 입력받아 BMI을 출력
#BMI = weight / (height ** 2)

YourHeight = float(input("당신의 키는:"))
YourWeight = float(input("당신의 몸무게는:"))
YourBMI = YourWeight / (YourHeight ** 2)
print(f"당신의 BMI지수는 {YourBMI:.2f}입니다.")

#5.반지름 입력시 원의 넓이와 둘레를 구하는 프로그램

R = float(input("원의 반지름:"))
round = R*2*3.14
weidth = 3.14 * (R ** 2)
print(f"이 원의 둘레는 {round:.2f}이고 원의 넓이는 {weidth:.2f}")


