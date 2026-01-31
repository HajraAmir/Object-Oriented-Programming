
class Polynomial:
    def __init__(self, dgr):
        self.coefficients = [0] * (dgr + 1)

    def __repr__(self):
        result = ""
        degree = len(self.coefficients) - 1
        for i in range(degree + 1):
            coeff = self.coefficients[i]
            if coeff != 0:
                if i == 0:
                    result += f"{coeff}"
                elif i == 1:
                    result += f" + {coeff}x"
                else:
                    result += f" + {coeff}x^{i}"
        return result

    def __len__(self):
        return len(self.coefficients) - 1

    def __mul__(self, n):
        result = Polynomial(len(self) + 1)
        for i in range(len(self.coefficients)):
            result.coefficients[i] = self.coefficients[i] * n
        return result

    def __rmul__(self, n):
        return self.__mul__(n)

    def eval(self, n):
        result = 0
        for i in range(len(self.coefficients)):
            result += self.coefficients[i] * (n ** i)
        return result

def main():
    p = Polynomial(3)
    p.coefficients = [1, 2, 3, 4]  # coefficients are in the order of x^0, x^1, x^2, ...

    print("Polynomial p(x):", p)
    print("Degree of p:", len(p))
    
    q = p * 2
    print("q = p * 2:", q)

    x_value = 2
    print("Evaluation of p at x =", x_value, ":", p.eval(x_value))


main()
