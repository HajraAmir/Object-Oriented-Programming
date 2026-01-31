class Callphone:
    def __init__(self,manufacturer,model,retail_price):
        self.__manufacturer=manufacturer
        self.__model=model
        self.__retail_price=retail_price
    def __repr__(self):
        return f'{self.__manufacturer} {self.__model} {self.__retail_price}'
    def set_manufacturer(self,manufacturer):
        self.__manufacturer= manufacturer
    def set_model(self,model):
        self.__model= model
    def set_retail_price(self,retail_price):
         self.__retail_price=retail_price
    def get_manufacturer(self):
        return self.__manufacturer
    def get_model(self):
        return self.__model
    def get_retail_price(self):
        return self.__retail_price
def main():
    print('Initial object:')
    call=Callphone("handcrafted","infinix hot",300000)
    print( call.get_model())
    print(call.get_manufacturer())
    print(call.get_retail_price())
    print("Updated objects:")
    call.set_model('galaxy')
    call.set_manufacturer('machine made')
    call.set_retail_price('400000')
    print( call.get_model())
    print(call.get_manufacturer())
    print(call.get_retail_price())
main()    