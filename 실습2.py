class Account:
    def __init__(self, name, money):
        """계좌의 소유주와 잔액을 설정합니다."""
        self.name=name
        self.money=money

    def deposit(self,plus):
        """계좌 입금"""
        if plus<0:
            print("금액은 양수여야 합니다.")
        else:
            self.money += plus
        print("%s원이 입금되었습니다."% plus)
    
    def withdraw(self, minus):
        """계좌 출금"""
        if minus>self.money:
            print("출금 금액이 잔액을 초과하거나 잘못 입력되었습니다.")
        else:
            self.money -= minus
        print("%s원이 출금되었습니다."% minus)
        
    def display_info(self):
        """계좌 잔액 정보를 표시합니다."""
        print("%s님의 계좌 잔액은 %d원입니다." % (self.name,  self.money))

# 계좌 인스턴스 생성
account1 = Account("가영", 1000)

# 계좌 정보 표시
account1.display_info()

account1.deposit(int(input()))

account1.withdraw(int(input()))

account1.display_info()