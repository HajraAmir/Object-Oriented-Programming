class footer:
    __address = 'Project Manager in Economic & Management French Departmant at RULE'

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
