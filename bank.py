

class Bank():
    account_number = ''
    account_holder =0
    balance=0

    def __init__(self,account_number,account_holder,initial_balance):
        self.account_number = account_number
        self.account_holder=account_holder
        self.initial_balance=initial_balance

    def __str__(self) -> str:
        print(f"Account Number : {self.account_number}")
        print(f"Account Holder : {self.account_holder}")
        print(f"Balance : {self.initial_balance}")
        return '--------------------------------------------------------------------------------'
    

    
    def deposit(self,amount):
        self.initial_balance += amount


    def withdraw(self, amount):
        if self.initial_balance < amount:
            print('ou gen {} HTG sou kont ou'.format(self.initial_balance))
            print('transaksyon sa pa ka fet paske kob ou gen sou kont ou an tro piti') 
        else:
            self.initial_balance -= amount


    def get_balance(self):
        print('balans ou se :',self.initial_balance)

#kreye kont
c1 = Bank('02ga5fx','Blanc Jorry',500)
print(c1) 
#depot
c1.deposit(300)
print(c1) 
#retrait
c1.withdraw(210)
print(c1) 

balance = c1.get_balance()