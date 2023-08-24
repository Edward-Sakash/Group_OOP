from task_2 import Car, Bike

if __name__ == "__main__":
    print('REGISTRATION APP FOR KEEPING RECORDS OF Vehicles\n')

    vehicles = []

    while True:
        print('1. Register Car')
        print('2. Register Bike')
        print('3. View Records')
        print('4. Exit')

        choice = input('Enter your choice: ')
        if choice == '1':
            reg_num = input("Enter car's registration number: ")
            power = input("Enter car's engine power: ")
            make = input("Enter car's make: ")
            model = input("Enter car's model: ")

            vehicles.append(Car(reg_num, power, make, model))

        elif choice == '2':
            reg_num = input("Enter motorcycle's registration number: ")
            power = input("Enter motorcycle's engine power: ")
            make = input("Enter motorcycle's make: ")
            model = input("Enter motorcycle's model: ")

            vehicles.append(Bike(reg_num, power, make, model))

        elif choice == '3':
            if len(vehicles) == 0:
                print('No Records!!\n\n')
            else:
                print("Vehicles Records:")
                for vehicle in vehicles:
                    vehicle.print_details()
                    print('\n')

        elif choice == '4':
            break
