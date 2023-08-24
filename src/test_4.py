from task_4 import Manager, Clerk

if __name__ == "__main__":
    while True:
        print("\n\n")
        print('1. Calculate Manager salary')
        print('2. Calculate Clerk salary')
        print('3. Exit')

        ch = input('Enter your choice: ')

        if ch == '1':
            name = input('Enter name: ')
            ID = input('Enter ID: ')
            base = float(input('Enter base salary: '))
            team_s = int(input('Enter team size: '))
            bonus = float(input("Enter bonus salary for manager: "))

            manager = Manager(name, ID, base, team_s, bonus)
            manager.calc_salary()
            print('Details:')
            manager.print_details()

        elif ch == '2':
            name = input('Enter name: ')
            ID = input('Enter ID: ')
            wage = float(input('Enter Hourly Salary: '))
            worked_hours = int(input("Enter the monthly number of hours: "))

            clerk = Clerk(name, ID, wage, worked_hours)
            clerk.calc_salary()
            print('Details')
            clerk.print_details()

        elif ch == "3":
            break
