class Callphone:
    def __init__(self,manufacturer,model,retail_price):
        self.__manufacturer=manufacturer
        self.__model=model
        self.__retail_price=retail_price
    def __repr__(self):
        return f'{self.__manufacturer} {self.__model} {self.__retail_price}'
    def set_manufacturer(self):
        return self.__manufacturer
    def set_model(self):
        return self.__model
    def set_retail_price(self):
        return self.__retail_price
    def get_manufacturer(self):
        return self.__manufacturer
    def get_model(self):
        return self.__model
    def get_retail_price(self):
        return self.__retail_price
def main():
    cell=("handcrafted","infinix hot",300000)
    cell.get__model()
    cell.get_manufacturer()
    cell.get_retail_price()
main()    