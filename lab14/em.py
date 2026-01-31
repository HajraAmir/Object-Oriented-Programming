class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}, Department: {self.department}")

class Executive(Employee):
    def __init__(self, name, department, monthly_salary, bonus=0):
        super().__init__(name, department)
        self.monthly_salary = monthly_salary
        self.bonus = bonus

    def calculate_net_salary(self):
        tax_deduction = 0.16 * self.monthly_salary
        return self.monthly_salary - tax_deduction + self.bonus

    def display_info(self):
        super().display_info()
        net_salary = self.calculate_net_salary()
        print(f"Monthly Salary: ${self.monthly_salary:.2f}, Bonus: ${self.bonus:.2f}, Net Salary after 16% Tax: ${net_salary:.2f}")

class Worker(Employee):
    def __init__(self, name, department, daily_rate, working_days, overtime_hours=0, overtime_rate=1.5):
        super().__init__(name, department)
        self.daily_rate = daily_rate
        self.working_days = working_days
        self.overtime_hours = overtime_hours
        self.overtime_rate = overtime_rate

    def calculate_monthly_income(self):
        regular_income = self.daily_rate * self.working_days
        overtime_income = self.daily_rate * self.overtime_hours * self.overtime_rate
        return regular_income + overtime_income

    def display_info(self):
        super().display_info()
        monthly_income = self.calculate_monthly_income()
        print(f"Daily Rate: ${self.daily_rate:.2f}, Working Days: {self.working_days}, Overtime Hours: {self.overtime_hours}, Monthly Income: ${monthly_income:.2f}")

def main():
    # Create some Executives
    exec1 = Executive("John Doe", "Finance", 8000, bonus=500)
    exec2 = Executive("Jane Smith", "Marketing", 9500, bonus=700)

    # Create some Workers
    worker1 = Worker("Alice Johnson", "Manufacturing", 100, 22, overtime_hours=10)
    worker2 = Worker("Bob Brown", "Maintenance", 120, 20, overtime_hours=5)

    # Display their information and monthly income
    print("Executives:")
    exec1.display_info()
    print()
    exec2.display_info()
    print("\nWorkers:")
    worker1.display_info()
    print()
    worker2.display_info()

if __name__ == "__main__":
    main()
