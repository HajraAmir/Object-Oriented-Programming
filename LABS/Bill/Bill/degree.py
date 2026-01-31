class degree:
    def __init__(self,dname,year,no):
        self.dname=dname
        self.year=year
        self.no=no
        
    
    @property
    def dname(self):
        return self.__dname     
    
    @dname.setter
    def dname(self,dname):
        self.dname=dname
    @property
    def year(self):
        return self.__year     
    
    @year.setter
    def dname(self,year):
        self.year=year    
    @property
    def no(self):
        return self.__no     
    
    @no.setter
    def dname(self,no):
        self.no=no      
        
    def __str__(self):
        return f'Degree: {self.dname} {self.no} {self.year}'  
        