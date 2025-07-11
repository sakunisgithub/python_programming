# Create a `BankAccount` class with attributes `account_holder` and `balance`. Add methods `deposit(amount)` and `withdraw(amount)`. Ensure the balance doesn't go negative on withdrawal.

class BankAccount :
    account_holder = 'person'
    balance = 0

    def __init__(self, holder_name, balance):
        self.account_holder = holder_name
        self.balance = balance

        print(f"Account opened ! Holder name : {holder_name}, Initial Balance : {balance}")
     
    def deposit(self, amount) :
        print(f"Amount {amount} deposited.")
        self.balance += amount
        print(f"Balance = {self.balance}")
    
    def withdraw(self, amount) :
        if self.balance >= amount : 
            print(f"Amount {amount} withdrawn.")
            self.balance -= amount
            print(f"Balance = {self.balance}")
        else :
            print("Insufficient Balance. Withdraw request rejected.")
            print(f"Balance = {self.balance}")


ananda = BankAccount('Ananda', 5000)

ananda.deposit(2000)

ananda.withdraw(500)

ananda.deposit(600)

ananda.withdraw(10000)

ananda.withdraw(100)