class Address:
    def __init__(self, hn, sn, town, city):
        self.Hn = hn
        self.Sn = sn
        self.Town = town
        self.City = city

    @property
    def Hn(self):
        return self.__hn
    
    @Hn.setter
    def Hn(self, hn):
        self.__hn = hn

    @property
    def Sn(self):
        return self.__sn
    
    @Sn.setter
    def Sn(self, sn):
        self.__sn = sn

    @property
    def Town(self):
        return self.__town
    
    @Town.setter
    def Town(self, town):
        self.__town = town

    @property
    def City(self):
        return self.__city
    
    @City.setter
    def City(self, city):
        self.__city = city

    def __str__(self):
        return f'Address: House # {self.Hn}, Street # {self.Sn}, {self.Town}, {self.City}.'
