class Mat2by2:
    def __init__(self, a11, a12, a21, a22):
        self.a11 = a11
        self.a12 = a12
        self.a21 = a21
        self.a22 = a22

    def __str__(self):
        return f"{self.a11},{self.a12},{self.a21},{self.a22}"

    @staticmethod
    def add(m1, m2):
        return Mat2by2(m1.a11 + m2.a11, m1.a12 + m2.a12, m1.a21 + m2.a21, m1.a22 + m2.a22)

    @staticmethod
    def sub(m1, m2):
        return Mat2by2(m1.a11 - m2.a11, m1.a12 - m2.a12, m1.a21 - m2.a21, m1.a22 - m2.a22)

    @staticmethod
    def mul(m1, m2):
        a11 = m1.a11 * m2.a11 + m1.a12 * m2.a21
        a12 = m1.a11 * m2.a11 + m1.a12 * m2.a12
        a21 = m1.a21 * m2.a11 + m1.a22 * m2.a21
        a22 = m1.a21 * m2.a11 + m1.a22 * m2.a22
        return Mat2by2(a11, a12, a21, a22)

    @staticmethod
    def determinant(m):
        return m.a11 * m.a22 - m.a12 * m.a21

    @staticmethod
    def is_identity(m):
        return m.a11 == 1 and m.a22 == 1 and m.a12 == 0 and m.a21 == 0

    @staticmethod
    def transpose(m):
        return Mat2by2(m.a11, m.a21, m.a12, m.a22)

def main():
    m1 = Mat2by2(1, 2, 3, 4)
    m2 = Mat2by2(5, 6, 7, 8)
    print('Matrix 1:', m1)
    print('Matrix 2:', m2)
    print('Addition of Matrices:', Mat2by2.add(m1, m2))
    print('Subtraction of Matrices:', Mat2by2.sub(m1, m2))
    print('Determinant:', Mat2by2.determinant(m1))
    print('Identity:', Mat2by2.is_identity(m1))
    print('Transpose of Matrices:', Mat2by2.transpose(m1))

main()
class Fruit:
    def _init_(self, name, uprice, uname, sucount, suname):
        self.__fruitName = name
        self.__unitPrice = uprice
        self.__unitName = uname
        self.__countInASaleUnit = sucount
        self.__saleUnitName = suname

    def _repr_(self):
        return f"{self.fruitName} ==> price: {self._unitPrice} per {self.unitName} saleable as {self._saleUnitName}s"

    def _str_(self):
        return self._repr_()

    def _eq_(self, other):
        return (
            self.fruitName == other.fruitName
            and self._unitPrice == other._unitPrice
            and self._unitName == other._unitName
            and self._countInASaleUnit == other._countInASaleUnit
            and self._saleUnitName == other._saleUnitName
        )

    def _ne_(self, other):
        return not self._eq_(other)

    def getFruitName(self):
        return self.fruitName

    def getUnitPrice(self):
        return self.__unitPrice

    def setUnitPrice(self, price):
        self.__unitPrice = price

    def getUnitName(self):
        return self.__unitName

    def setUnitName(self, name):
        self.__unitName = name

    def getCountInASaleUnit(self):
        return self.__countInASaleUnit

    def setCountInASaleUnit(self, count):
        self.__countInASaleUnit = count

    def getSaleUnitName(self):
        return self.__saleUnitName

    def setSaleUnitName(self, name):
        self.__saleUnitName = name

    def payment(self, units):
        return units * self._unitPrice * self._countInASaleUnit


def main():
    k = Fruit("Kela", 36, "unit", 12, "dozen")
    t = Fruit("Turbooz", 25, "kg", 1, "kg")
    m = Fruit("Mango", 50, "unit", 6, "piece")

    print("available fruits")
    print(t)
    print(k)
    print(m)

    print(k == t) 
    print(k != t) 

    print(k.getFruitName(), "of quantity 2.5 costs", k.payment(2.5))
    print(t.getFruitName(), "of quantity 5 costs", t.payment(5))
    print(m.getFruitName(), "of quantity 3 costs", m.payment(3))

main()