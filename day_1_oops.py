class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount

        else:
            print("insufficient balance")

    def show_balance(self):
        print("owner:",self.owner,"Balance:",self.balance)


class SavingsAccount(Account):
    def __init__(self,owner,balance,interest_rate):
        super().__init__(owner,balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.interests = self.balance * self.interest_rate /100
        self.balance +=self.interests

s1 = SavingsAccount("Naveen",1000,10)
s1.deposit(500)
s1.withdraw(300)
s1.add_interest(10)
s1.show_balance()

        

    

    
