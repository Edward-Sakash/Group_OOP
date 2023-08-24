from task_1 import Person, Student, Teacher

if __name__ == "__main__":
    print('REGISTRATION APP FOR KEEPING RECORDS OF REGISTERED STUDENTS AND TEACHERS\n')

    persons = []

    while True:
        print('1. Register Student')
        print('2. Register Teacher')
        print('3. View Records')
        print('4. Exit')

        choice = input('Enter your choice: ')
        if choice == '1':
            name = input("Enter Student's Name: ")
            age = int(input("Enter Student's Age: "))
            ID = input("Enter Student's ID: ")
            gpa = float(input("Enter Student's GPA: "))

            persons.append(Student(name, age, ID, gpa))

        elif choice == '2':
            name = input("Enter Teacher's Name: ")
            age = int(input("Enter Teacher's Age: "))
            ID = input("Enter Teacher's ID: ")
            specialization = input("Enter Teacher's Specialization: ")

            persons.append(Teacher(name, age, ID, specialization))

        elif choice == '3':
            if len(persons) == 0:
                print('No Records!!')
            else:
                print("Students and Teachers Records:")
                for person in persons:
                    person.print_details()
                    print('\n')

        elif choice == '4':
            break
