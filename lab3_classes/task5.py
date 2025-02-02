class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner #owner
        self.balance = balance  #balanse
    
    def deposit(self, amount):#deposit
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("it must be positive.")
    
    def withdraw(self, amount):#withdraaw
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Withdrawal exceeds balance.")
        else:
            print("it must be positive.")

account = Account("Tony", 100)

account.deposit(50)  
account.withdraw(30)  
account.withdraw(200) 
account.deposit(-10)  
account.withdraw(-20) 
