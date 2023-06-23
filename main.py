
class BankAccount:
    def __init__(self,account_number, summ):
        self.account_number = account_number
        self.summ = summ
    def deposit(self,a):
        self.summ = self.summ + a
        return self.summ
    def withdraw(self,a):
        self.summ = self.summ - a
        return self.summ 
    def get_balance(self):
        return self.summ
        

account =  BankAccount('12',2000.0) 


print(account.summ)
print(account.account_number)
print(account.deposit(15.0))
print(account.withdraw(5.0))
balance = account.get_balance()
print(f'Current balance:${balance}')



        