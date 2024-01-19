# class_practice - 3

class Dog:
    # 구조체는 수정 불가
    def __init__(self, n):
        self.hp = 100 # max 200
        self.stress = 50 # max 100
        self.name = n
    # 함수의 존재 이유는 구조체 데이터 보호
    def eating(self):
        if(self.hp >= 200):
            print(f"체력이 꽉 찼습니다.\n현재 체력은 {self.hp} 입니다.")
            self.hp = 200
        else:
            print(f"현재 체력은 {self.hp} 입니다.")
            self.hp += 50
a = Dog('mega')
a.eating()
a.eating()
a.eating()
a.eating()
a.eating()
a.eating()
a.eating()
a.eating()
