class Fruit:
    def __init__(self, name, uprice, uname, sucount, suname):
        # self, the object just constructed and in initiazilation 
        # name, name of the fruit, e.g. Kela, Amrood, etc
        # uprice, unit price of fruit
        # uname, unit name e.g. unit, piece, kg, meter, etc
        # sucount, count in sale unit, e.g., for dozen it is 12, for pack it may be 4,5 or 10, etc
        # suname, sale unit e.g. dozens, kgs, meters, etc

        self.__fruitName = name
        self.__unitPrice = uprice
        self.__unitName = uname
        self.__countInASaleUnit = sucount
        self.__saleUnitName = suname

    def __repr__(self):
        # self, the object to be represented at a sequence of bytes
        return f"{self.__fruitName} ==> price: {self.__unitPrice} per {self.__unitName} saleble as {self.__saleUnitName}s"

    def __str__(self):
        # self, the object to be represented at a sequence of characters
        return self.__repr__()

    def getFruitName(self):
        # self, the object in context
        return self.__fruitName

    def payment(self, units):
        # self, the object under sale
        # units, how many units under the sale
        return units * self.__unitPrice * self.__countInASaleUnit

def main():
    k = Fruit("Kela", 35, "unit", 12, "dozen")
    t = Fruit("Turbooz", 25, "kg", 1, "kg")
    
    print("available fruits")
    print(t)
    print(k)
    
    print(k.getFruitName(), "of quantity 2.5 costs", k.payment(2.5))
    print(t.getFruitName(), "of quantity 5 costs", t.payment(5))

main()