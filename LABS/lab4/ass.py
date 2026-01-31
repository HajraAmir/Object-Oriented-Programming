class BillItem:
    def __init__(self, prt, rte, qty):
        self.__pirticular = prt
        self.__unitprice = rte
        self.__quantity = qty

    def __str__(self):
        particular = self.__pirticular.ljust(25)
        rate = f"{self.__unitprice:.1f}".rjust(10)
        quantity = str(self.__quantity).rjust(4)
        amount = f"{self.__unitprice * self.__quantity:.1f}".rjust(8)
        return f"{particular}{rate}{quantity}{amount}"
