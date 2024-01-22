class BankAccount:
    def __init__(self, account_number, owner_name):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            print("금액을 잘못 입력 하였습니다.")
            return False

    def withdraw(self, amount):
        if 0 < amount and amount < self.balance:
            self.balance -= amount
            return True
        else:
            print("금액을 잘못 입력 하였습니다.")
            return False

    def get_balance(self):
        return self.balance

    def get_account(self):
        return f"Account: {self.account_number}\nOwner: {self.owner_name}\nbalance: {self.balance}"

def bankSystem():

    globalAccount = {}

    while True:
        print("은행 계좌 시스템\n1: 계좌 개설\n2: 입금\n3: 출금\n4: 잔액 조회\n5: 종료")
        systemNumber = input("선택. ")

        if systemNumber == "1":
            account_number = input("계좌 번호. ")
            owner_name = input("소유자 이름. ")
            globalAccount[account_number] = BankAccount(account_number, owner_name)
            print("계좌 개설이 완료 되었습니다.")

        elif systemNumber == "2":
            account_number = input("계좌 번호 입력. ")
            amount = int(input("입금액. "))
            if account_number in globalAccount and globalAccount[account_number].deposit(amount):
                print("입금 완료.")
            else:
                print("입금 실패.")

        elif systemNumber == "3":
            account_number = input("계좌 번호 입력. ")
            amount = int(input("출금액. "))
            if account_number in globalAccount and globalAccount[account_number].withdraw(amount):
                print("출금 완료.")
            else:
                print("출금 실패.")

        elif systemNumber == "4":
            account_number = input("계좌 번호 입력. ")
            if account_number in globalAccount:
                print(globalAccount[account_number].get_account())
            else:
                print("계좌를 찾을 수 없습니다.")

        elif systemNumber == "5":
            print("프로그램을 종료합니다.")
            break

        else:
            print("옳은 번호를 입력하세요.")

bankSystem()

class KakaoBankAccount(BankAccount):
    pass

a = KakaoBankAccount()
a.deposit()