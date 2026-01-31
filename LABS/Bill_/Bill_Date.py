class Date:
    def __init__(self, date = None, month = None, year = None):
        self.Date = date
        self.Month = month
        self.Year = year
        return 
    
    @property
    def Date(self):
        return self.__date
    
    @Date.setter
    def Date(self, date):
        self.__date = date

    @property
    def Month(self):
        return self.__month
    
    @Month.setter
    def Month(self, month):
        self.__month = month

    @property
    def Year(self):
        return self.__year
    
    @Year.setter
    def Year(self, year):
        self.__year = year

    def __str__(self):
        return f'Date: {self.Date}/{self.Month}/{self.Year}'
