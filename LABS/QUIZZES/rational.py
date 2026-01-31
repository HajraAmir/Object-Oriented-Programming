from math import gcd

class RationalNumber:
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self._numerator = numerator
        self._denominator = denominator
        self._simplify()

    def __repr__(self):
        return f"{self._numerator}|{self._denominator}"

    def __str__(self):
        return f"{self._numerator}/{self._denominator}"

    def _simplify(self):
        common_divisor = gcd(self._numerator, self._denominator)
        self._numerator //= common_divisor
        self._denominator //= common_divisor

    def simplify(self):
        self._simplify()

    def reciprocal(self):
        return RationalNumber(self._denominator, self._numerator)

    def to_integer(self):
        return self._numerator // self._denominator

    def to_float(self):
        return self._numerator / self._denominator

    def to_bool(self):
        return bool(self._numerator)

    def to_string(self):
        return str(self)

    def absolute_value(self):
        return RationalNumber(abs(self._numerator), self._denominator)

    def arithmetic_inverse(self):
        return RationalNumber(-self._numerator, self._denominator)

    def power(self, exponent):
        if isinstance(exponent, int):
            return RationalNumber(self._numerator ** exponent, self._denominator ** abs(exponent))
        else:
            raise TypeError("Exponent must be an integer")

    def __abs__(self):
        return self.absolute_value()

    def __add__(self, other):
        if isinstance(other, RationalNumber):
            common_denominator = self._denominator * other._denominator
            new_numerator = (self._numerator * other._denominator) + \
                            (other._numerator * self._denominator)
            return RationalNumber(new_numerator, common_denominator)
        else:
            raise TypeError("Unsupported operand type for +")


    def __sub__(self, other):
        if isinstance(other, RationalNumber):
            return self + RationalNumber(-other._numerator, other._denominator)
        elif isinstance(other, (int, float)):
            return self - RationalNumber(other)
        else:
            raise TypeError("Unsupported operand type for -")

    def __mul__(self, other):
        if isinstance(other, RationalNumber):
            return RationalNumber(self._numerator * other._numerator,
                                  self._denominator * other._denominator)
        elif isinstance(other, (int, float)):
            return self * RationalNumber(other)
        else:
            raise TypeError("Unsupported operand type for *")

    def __truediv__(self, other):
        if isinstance(other, RationalNumber):
            return self * other.reciprocal()
        elif isinstance(other, (int, float)):
            return self / RationalNumber(other)
        else:
            raise TypeError("Unsupported operand type for /")

    def __eq__(self, other):
        if isinstance(other, RationalNumber):
            return (self._numerator == other._numerator) and (self._denominator == other._denominator)
        elif isinstance(other, (int, float)):
            return self == RationalNumber(other)
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, RationalNumber):
            return (self._numerator * other._denominator) < (other._numerator * self._denominator)
        elif isinstance(other, (int, float)):
            return self < RationalNumber(other)
        else:
            raise TypeError("Unsupported operand type for <")

    def __le__(self, other):
        if isinstance(other, RationalNumber):
            return self < other or self == other
        elif isinstance(other, (int, float)):
            return self <= RationalNumber(other)
        else:
            raise TypeError("Unsupported operand type for <=")

    def __gt__(self, other):
        if isinstance(other, RationalNumber):
            return not (self <= other)
        elif isinstance(other, (int, float)):
            return self > RationalNumber(other)
        else:
            raise TypeError("Unsupported operand type for >")

    def __ge__(self, other):
        if isinstance(other, RationalNumber):
            return not (self < other)
        elif isinstance(other, (int, float)):
            return self >= RationalNumber(other)
        else:
            raise TypeError("Unsupported operand type for >=")
def main():
    r1 = RationalNumber(2, 3)
    r2 = RationalNumber(4, 5)
    print("Integer value of r1:", r1.to_integer()) 
    print("Float value of r2:", r2.to_float())      
    print("Boolean value of r1:", r1.to_bool())     
    print("String representation of r2:", r2.to_string()) 
    print("Absolute value of r1:", abs(r1))              
    print("Arithmetic inverse of r2:", r2.arithmetic_inverse())  
    print("r1 raised to the power of 2:", r1.power(2))       
    print("Addition of r1 and r2:", r1 + r2)  
    print("Subtraction of r1 and r2:", r1 - r2) 
    print("Multiplication of r1 and r2:", r1 * r2)  
    print("Division of r1 and r2:", r1 / r2)  
    print("Is r1 equal to 3/4?", r1 == RationalNumber(3, 4))  
    print("Is r1 not equal to r2?", r1 != r2)                
    print("Is r1 less than r2?", r1 < r2)                   
    print("Is r2 less than or equal to r2?", r2 <= r2)      
    print("Is r1 greater than r2?", r1 > r2)                 
    print("Is r2 greater than or equal to r1?", r2 >= r1)   
main()