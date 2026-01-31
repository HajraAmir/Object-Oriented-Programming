class Items:
    def __init__(self, quan, item, rate):
        self.Quantity = quan
        self.Item = item
        self.Rate = rate

    @property
    def Quantity(self):
        return self.__quan
    
    @Quantity.setter
    def Quantity(self, quan):
        self.__quan = quan

    @property
    def Item(self):
        return self.__item
    
    @Item.setter
    def Item(self, item):
        self.__item = item

    @property
    def Rate(self):
        return self.__rate
    
    @Rate.setter
    def Rate(self, rate):
        self.__rate = rate
    
    def __str__(self):
        return f'{self.Quantity},{self.Item},{self.Rate},{int(self.Quantity) * int(self.Rate)}'

