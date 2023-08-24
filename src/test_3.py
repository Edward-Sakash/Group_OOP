from task_3 import CheckingAccount, SavingsAccount


if __name__ == "__main__":
    print("1. Create Savings Account")
    print('2. Create Checking Account')
    choice = input('Enter your choice: ')

    Account = None

    if choice == '1':
        print("\n\n")
        number = input('Enter Account number: ')
        balance = float(input('Enter balance: '))
        rate = float(input('Enter interest Rate: '))
        account = SavingsAccount(number, balance, rate)

    elif choice == '2':
        acc_num = input('Enter Account number: ')
        balance = float(input('Enter balance: '))
        transactions = int(input('Enter number of allowed transactions: '))

        account = CheckingAccount(acc_num, balance, transactions)
    else:
        print("Wrong choice")
        exit()

    while True:
        print("\n")
        print('1. Check Current Balance')
        print('2. Deposit Amount')
        print('3. Withdraw Amount')
        print('4. Next Month')
        print('5. Exit')

        ch = input('Enter your choice: ')

        if ch == '1':
            print(account)
        elif ch == '2':
            am = float(input('Enter amount: '))
            account.deposit(am)
        elif ch == '3':
            am = float(input('Enter amount: '))
            account.withdraw(am)
        elif ch == '4':
            account.next_month()
        elif ch == '5':
            break
