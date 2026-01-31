class Name:
    def __init__(self, fn, ln):
        self.Fn = fn
        self.Ln = ln

    @property
    def Fn(self):
        return self.__fn
    
    @Fn.setter
    def Fn(self, fn):
        self.__fn = fn

    @property
    def Ln(self):
        return self.__ln
    
    @Ln.setter
    def Ln(self, ln):
        self.__ln = ln

    def __str__(self):
        return f'Name: {self.Fn} {self.Ln}'
