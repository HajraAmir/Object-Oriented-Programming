class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department
class Executive(Employee):
    def __init__(self, name, department, salary):
        super().__init__(name, department)
        self.salary = salary
    def calculate_monthly_income(self):
        tax_deduction = 0.16 * self.salary
        return self.salary - tax_deduction
class Worker(Employee):
    def __init__(self, name, department, pay_rate, days_worked):
        super().__init__(name, department)
        self.pay_rate = pay_rate
        self.days_worked = days_worked  
    def calculate_monthly_income(self):
        return self.pay_rate * self.days_worked
exe1 = Executive("Smith Doe", "Finance", 10000)
exe2 = Executive("Jane Smith", "Marketing", 12000)
exe3 = Executive("wardth", "Finance", 15000)
exe4 = Executive("Alan", "accounting", 14000)
worker1 = Worker("Alice Johnson", "Production", 50, 20)
worker2 = Worker("Williams john", "IT", 60, 25)
worker3 = Worker("Alen frank", "management", 90, 10)
worker4 = Worker("Ward alen", "pharmacy", 40, 25)
print(f"{exe1.name}'s monthly income: ${exe1.calculate_monthly_income():.2f}")
print(f"{exe2.name}'s monthly income: ${exe2.calculate_monthly_income():.2f}")
print(f"{exe3.name}'s monthly income: ${exe3.calculate_monthly_income():.2f}")
print(f"{exe4.name}'s monthly income: ${exe4.calculate_monthly_income():.2f}")
print(f"{worker1.name}'s monthly income: ${worker1.calculate_monthly_income():.2f}")
print(f"{worker2.name}'s monthly income: ${worker2.calculate_monthly_income():.2f}")
print(f"{worker3.name}'s monthly income: ${worker3.calculate_monthly_income():.2f}")
print(f"{worker4.name}'s monthly income: ${worker4.calculate_monthly_income():.2f}")