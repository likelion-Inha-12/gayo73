from 실습2 import Account

class SavingAccount(Account):
    def __init__(self, name, money, interest):
        """이자"""
        super().__init__(name, money)
        self.interest=interest

    def display_balance(self):
        """계좌 잔액 정보를 표시합니다."""
        print("%s님의 계좌 잔액은 %d원입니다." % (self.name,  self.money))
        print("이자율: %.1f%%"%(self.interest*100))

    def add_interest(self):
        """이자 추가"""
        interest_amount=int(self.money*self.interest)
        self.money+=interest_amount
        print("%s님의 계좌에 %d원의 이자가 추가되었습니다."%(self.name, interest_amount))
        

saving_account = SavingAccount("가영", 1000, 0.05)

saving_account.display_balance()

saving_account.deposit(500)

saving_account.add_interest()

saving_account.withdraw(100)

saving_account.display_balance()