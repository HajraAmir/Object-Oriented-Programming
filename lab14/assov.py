class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

class Customer:
    def __init__(self, name):
        self.name = name

# Example usage
bank = Bank("ABC Bank")

customer1 = Customer("Alice")
customer2 = Customer("Bob")

# Associate customers with the bank
bank.add_customer(customer1)
bank.add_customer(customer2)

# Display bank's customers
print(f"{bank.name} customers:")
for customer in bank.customers:
    print(customer.name)
