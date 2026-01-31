class Bill_header:
    __domain = 'MOBILO'
    __shop = 'MOBILE CITY'
    __quote = 'Deals in all kinds of Mobiles and Accessories'
    __cell = 'Cell: 0315-0000000'
    __idk = 'Case Memo'
    
    def __init__(self, nmbr):
        self.Nmbr = nmbr
        
    @property
    def Nmbr(self):
        return self.__nmbr
    
    @Nmbr.setter
    def Nmbr(self, nmbr):
        self.__nmbr = nmbr
    
    def __str__(self):
         return f' \t\t\t{self.__domain}\n\t\t     {self.__shop}\n\t{self.__quote}\n\t\t   {self.__cell}\n\t\t       {self.__idk}\n\nNo. : {self.Nmbr}' 
