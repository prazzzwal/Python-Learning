# **Question:**
# You create a parent class `Account` that stores a private variable `_balance` and provides getter and setter methods. 
# Then you create a child class `SavingsAccount` with its own constructor.

# 1. What problem will occur if `SavingsAccount` does not call `super().__init__()`?
# 2. How does this affect encapsulation of `_balance`?
# 3. Why can the getter and setter of `Account` fail even though they are inherited by `SavingsAccount`?

# This tests understanding of:

# * Encapsulation
# * Constructor overriding
# * Role of `super()`
# * Inherited access control logic



class Account:
    def __init__(self):
        self._balance = 5000

    #getter
    @property
    def balance(self):
        return self._balance 

    #setter
    @balance.setter
    def balance(self,value):
        self._balance = value

class SavingAccount(Account):
    def __init__(self):
        super().__init__()
        self._accType = "Savings"

    def info(self):
        print(f"Account Type : {self._accType}")


a1 = Account()

s1 = SavingAccount()


print(a1._balance)

print(s1._Account_balance)