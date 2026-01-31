from datetime import datetime

class Address:
    def __init__(self, address):
        self.__address = address

    def __str__(self):
        return self.__address

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

class BillItem:
    def __init__(self, prt, rte, qty):
        self.__pirticular = prt
        self.__unitprice = rte
        self.__quantity = qty

    def __str__(self):
        return f"{self.__pirticular.ljust(25)}{str(self.__unitprice).ljust(6)}{str(self.__quantity).ljust(7)}{str(self.__unitprice*self.__quantity)}"

    def get_particular(self):
        return self.__pirticular

    def set_particular(self, particular):
        self.__pirticular = particular

    def get_unitprice(self):
        return self.__unitprice

    def set_unitprice(self, unitprice):
        self.__unitprice = unitprice

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity

class Bill:
    def __init__(self, no, dt, nm, ad, ib):
        self.__billno = no
        self.__billdate = dt
        self.__custname = nm
        self.__custaddr = ad
        self.__items = []
        self.__items.extend(ib)

    def __str__(self):
        rs = f"MOBILO\nMobile City\nDeals in all kinds of Mobile sets and Accessories\nCell No: 0321-0000000\n\nCASHMENO\nNo: {self.__billno}\nDate: {self.__billdate.strftime('%d-%m-%Y')}\nCustomer Name: {self.__custname}\nCustomer Address: {self.__custaddr}\n\nPirticulars                Rate    Qty      Amount\n"
        for itm in self.__items:
            rs = rs + str(itm) + '\n'
        rs += "\n" + " " * 57 + f"Total {self.calculate_total()}"
        return rs

    def calculate_total(self):
        total = sum(item.get_unitprice() * item.get_quantity() for item in self.__items)
        return total

def main():
    
    num = input('Enter the bill number: ')
    date_str = input('Enter the bill date (DD-MM-YYYY): ').strip()
    nam = input('Enter the customer name: ')
    addr = input('Enter the customer address: ')

    num_of_items = int(input('Enter the number of items: '))
    items = []
    for i in range(num_of_items):
        particular = input(f'Enter the particular for item {i+1}: ')
        rate = float(input(f'Enter the rate for item {i+1}: '))
        quantity = int(input(f'Enter the quantity for item {i+1}: '))
        items.append(BillItem(particular, rate, quantity))

    b = Bill(num, datetime.strptime(date_str, "%d-%m-%Y"), nam, Address(addr), items)

    print(b)

main()