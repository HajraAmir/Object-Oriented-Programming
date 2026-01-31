class Bill_footer:
    __address = 'Shop Address: Basement # 2, Allah Wala Plaza, G-9 Markaz, Islamabad'

    def __init__(self, sign):
        self.Sign = sign

    @property
    def Sign(self):
        return self.__sign
    
    @Sign.setter
    def Sign(self, sign):
        self.__sign = sign

    def __str__(self):
     return f'Signature: {self.Sign}\n{self.__address}'
