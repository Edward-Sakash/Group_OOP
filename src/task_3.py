class BankAccount:
    def __init__(self, acc_num, balance):
        self.acc_num = acc_num
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def __str__(self):
        return f"Account Number: {self.acc_num}\nBalance: {self.balance:.2f}"


class SavingsAccount(BankAccount):
    def __init__(self, acc_num, balance, interest_rate):
        super().__init__(acc_num, balance)
        self.interest_rate = interest_rate

    def next_month(self):
        self.balance += self.balance * (self.interest_rate / 100)

    def __str__(self):
        return super().__str__() + f"\nInterest Rate: {self.interest_rate}%"


class CheckingAccount(BankAccount):
    def __init__(self, acc_num, balance, no_transaction):
        super().__init__(acc_num, balance)
        self.no_transaction = no_transaction
        self.transaction_count = 0

    def deposit(self, amount):
        if self.transaction_count < self.no_transaction:
            super().deposit(amount)
            self.transaction_count += 1

    def withdraw(self, amount):
        if self.transaction_count < self.no_transaction:
            if super().withdraw(amount):
                self.transaction_count += 1
                return True
        return False

    def next_month(self):
        self.transaction_count = 0

    def __str__(self):
        return super().__str__() + f"\nMax Transactions: {self.no_transaction}"


# Example usage
if __name__ == "__main__":
    savings = SavingsAccount("SA123", 1000, 2)
    checking = CheckingAccount("CA456", 500, 5)

    print("Initial Details:")
    print(savings)
    print(checking)

    savings.deposit(200)
    checking.deposit(100)
    checking.withdraw(50)
    checking.withdraw(30)

    print("\nDetails after Transactions:")
    print(savings)
    print(checking)

    savings.next_month()
    checking.next_month()

    print("\nDetails after Next Month:")
    print(savings)
    print(checking)
