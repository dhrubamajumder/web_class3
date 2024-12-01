class MobileBankingAccount:
    def __init__(self, account_number, account_holder, pin, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        return f"Account holder: {self.account_holder}, Account No: {self.account_number}\nBalance: {self.balance} units"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Successfully deposited {amount} units. New balance: {self.balance} units."
        return "Deposit amount must be positive."

    def withdraw(self, amount, pin):
        if pin != self.pin:
            return "Incorrect PIN."
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Successfully withdrew {amount} units. New balance: {self.balance} units."
        if amount > self.balance:
            return "Insufficient balance."
        return "Withdrawal amount must be positive."

    def transfer(self, target_account, amount, pin):
        if pin != self.pin:
            return "Incorrect PIN."
        if 0 < amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            return f"Transferred {amount} units to {target_account.account_holder} (Account No: {target_account.account_number})."
        if amount > self.balance:
            return "Insufficient balance for the transfer."
        return "Transfer amount must be positive."


# Banking System Management
class MobileBankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder, pin, initial_deposit=0):
        if account_number in self.accounts:
            return "Account number already exists!"
        new_account = MobileBankingAccount(account_number, account_holder, pin, initial_deposit)
        self.accounts[account_number] = new_account
        return f"Account for {account_holder} created successfully with balance {initial_deposit} units."

    def get_account(self, account_number, pin):
        if account_number in self.accounts and self.accounts[account_number].pin == pin:
            return self.accounts[account_number]
        return "Account not found or incorrect PIN."


# Sample Interface for Mobile Banking
def run_banking_system():
    system = MobileBankingSystem()

    while True:
        print("\n=== Mobile Banking System ===")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            account_number = input("Enter new account number: ")
            account_holder = input("Enter account holder name: ")
            pin = input("Set a 4-digit PIN: ")
            initial_deposit = float(input("Enter initial deposit: "))
            print(system.create_account(account_number, account_holder, pin, initial_deposit))

        elif choice == '2':
            account_number = input("Enter account number: ")
            pin = input("Enter PIN: ")
            account = system.get_account(account_number, pin)
            if isinstance(account, MobileBankingAccount):
                print(account.check_balance())
            else:
                print(account)

        elif choice == '3':
            account_number = input("Enter account number: ")
            pin = input("Enter PIN: ")
            account = system.get_account(account_number, pin)
            if isinstance(account, MobileBankingAccount):
                amount = float(input("Enter deposit amount: "))
                print(account.deposit(amount))
            else:
                print(account)

        elif choice == '4':
            account_number = input("Enter account number: ")
            pin = input("Enter PIN: ")
            account = system.get_account(account_number, pin)
            if isinstance(account, MobileBankingAccount):
                amount = float(input("Enter withdrawal amount: "))
                print(account.withdraw(amount, pin))
            else:
                print(account)

        elif choice == '5':
            account_number = input("Enter your account number: ")
            pin = input("Enter PIN: ")
            account = system.get_account(account_number, pin)
            if isinstance(account, MobileBankingAccount):
                target_account_number = input("Enter recipient account number: ")
                if target_account_number in system.accounts:
                    target_account = system.accounts[target_account_number]
                    amount = float(input(f"Enter amount to transfer to {target_account.account_holder}: "))
                    print(account.transfer(target_account, amount, pin))
                else:
                    print("Recipient account not found.")
            else:
                print(account)

        elif choice == '6':
            print("Exiting Mobile Banking System. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


# Run the banking system
run_banking_system()
