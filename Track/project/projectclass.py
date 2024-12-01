# --------------------------------
# Mobile banking  
# --------------------------------

# class Banking:
#     def __init__(self, user_name, initial_balance):
#         self.name = user_name
#         self.balance = initial_balance

#     def deposit(self, amount):
#         if amount>0:
#             self.balance += amount
#         return amount
        
#     def get_balance(self):
#         return self.balance

#     def withdraw(self, amount):
#         if amount < self.balance:
#             self.balance -= amount
#             self.balance -= amount

# ostad = Banking("Ostad", 1000)
# print(f"Account Name: {ostad.name}")
# print(f"Inital Balance is: {ostad.balance}")


# -------------------------------------

# class BankAccount:
#     def __init__(self,account_holder, balance ,age):
#         self.account_holder = account_holder
#         self.balance = balance
#         self.age = age
#     def deposit(self,amount):
#         if amount < 0 :
#             print("Invalid amount")
#         else:
#             self.balance+=amount
#             print("Amount deposit successfully ")
#     def withdraw(self,amount):
#         if amount >self.balance:
#             print("Insufficient amount")
#         else:
#             self.balance -=amount
#             print(f"Withdraw : {amount} New balance : {self.balance}")
#     def check_balance(self):
#         print(f"Account holder:{self.account_holder} , Balance: {self.balance} year:{self.age}")


# account = BankAccount("Rahim",1000 ,5)
# account.deposit(500)
# account.check_balance()
# account.withdraw(400)





# --------------------------------------------------------
#               User Input 
# ---------------------------------------------

class Banking:
    def __init__(self, user_name, initial_balance):
        self.name = user_name
        self.balance = initial_balance
       
        
    def deposit(self, amount):
        if amount>0:
            self.balance += amount
        return amount
    
    def get_balance(self):
        return self.balance
    
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            return amount
        else:
            return f'Insufficient Balance'

ostad = Banking("Ostad", 10000)
print(f"Account Name : {ostad.name}")
print(f"Initial Balance is :{ostad.balance}")
print(f"Deposit Balance :{ostad.deposit(1000)}")
print(f"After deposit, Your Balance is : {ostad.get_balance()}")
print(f"Withdraw Balance : {ostad.withdraw(2000)}")
print(f"After withdraw, Your Balance is : {ostad.get_balance()}")

