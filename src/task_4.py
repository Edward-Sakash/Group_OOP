class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def get_salary(self):
        return self.salary

    def print_details(self):
        print(f"Employee: {self.name}, ID: {self.emp_id}, Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, emp_id, base_salary, team_size, bonus):
        super().__init__(name, emp_id, 0)  # Initialize salary as 0
        self.base_salary = base_salary
        self.team_size = team_size
        self.bonus = bonus
        self.calc_salary()  # Calculate and set the salary

    def calc_salary(self):
        self.salary = self.base_salary + (self.team_size * self.bonus)

    def print_details(self):
        super().print_details()
        print(f"Base Salary: {self.base_salary}, Team Size: {self.team_size}, Bonus: {self.bonus}")


class Clerk(Employee):
    def __init__(self, name, emp_id, hourly_wage, num_hours):
        super().__init__(name, emp_id, 0)  # Initialize salary as 0
        self.hourly_wage = hourly_wage
        self.num_hours = num_hours
        self.calc_salary()  # Calculate and set the salary

    def calc_salary(self):
        self.salary = self.hourly_wage * self.num_hours

    def print_details(self):
        super().print_details()
        print(f"Hourly Wage: {self.hourly_wage}, Number of Hours: {self.num_hours}")


# Example usage
manager = Manager("John", 101, 50000, 10, 1000)
manager.print_details()

clerk = Clerk("Jane", 102, 15, 40)
clerk.print_details()
