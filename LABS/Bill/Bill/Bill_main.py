from Bill_Name import Name
from Bill_Date import Date
from Bill_Address import Address
from Bill_Items import Items
from Bill_Header import Bill_header
from Bill_Footer import Bill_footer

def main():

    #Name
    first = input('Enter First Name: ')
    last = input('Enter Last Name: ')
    n = Name(first, last)
    
    #Address
    house = input('Enter House no. : ')
    street = input('Enter Street no. : ')
    town = input('Enter Town: ') 
    city = input('Enter City: ')
    a = Address(house, street, town, city)
    
    #Date
    try:    
        date, month, year = input('Enter Date: ').split('/')
        d = Date(date, month, year)
    except:
        print('Invalid date format. Please use format: DD/MM/YY')

    #Items
    total = 0
    l = []
    for i in range (int(input('Number of items: '))):
        amount = 0    
        quantity = input(f'Enter Quantity of item {i+1}: ')
        item = input(f'Enter Item {i+1}: ')
        rate = input(f'Enter Rate of Item {i+1}: ')
        amount = int(quantity) * int(rate)
        it = Items(quantity, item, rate)
        total += amount
        l.append(str(it).split(','))
    
    #Bill Header
    nmbr = input('Enter Invoice No. : ')
    bh = Bill_header(nmbr)
    
    #Bill Footer
    s = input('Enter Signature: ')
    bf = Bill_footer(s)
    
    #Printing
    print()
    print(bh)
    print()
    print(n,'\t\t',d)
    print(a)
    print()
    print('-----------------------------------------------------')
    print('Qty.\tParticulars\t\tRate\tAmount')
    print('-----------------------------------------------------')
    for i in range (len(l)):
        for j in range (4):
            if j != 1:
                print(l[i][j],end='\t')
            else:
                print(l[i][j],end='\t\t')
        print()
    print('-----------------------------------------------------')
    print('\t\t\t\t\tTotal: ',total)
    print('-----------------------------------------------------')
    print()
    print(bf)
    print()

if __name__ == '__main__':
    main()