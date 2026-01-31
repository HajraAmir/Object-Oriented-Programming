class Polynomial:
    def __init__(self, coefficients):
        # Initialize the Polynomial with a list of coefficients. 
        # The coefficient at index i corresponds to the term of x^i.
        self.coefficients = coefficients[:]  # Make a shallow copy to avoid aliasing

    def __repr__(self):
        # Representation of the polynomial in a readable format
        return "Polynomial(" + str(self.coefficients) + ")"

    def __getitem__(self, index):
        # Allows getting a coefficient using the index notation
        return self.coefficients[index]

    def __setitem__(self, index, value):
        # Allows setting a coefficient using the index notation
        self.coefficients[index] = value

    def __eq__(self, other):
        # Checks if two polynomials are equal by comparing their coefficients
        return self.coefficients == other.coefficients

    def __lt__(self, other):
        # Check if the degree of this polynomial is less than the other
        return len(self.coefficients) < len(other.coefficients)

    def degree(self):
        # Returns the degree of the polynomial
        return len(self.coefficients) - 1

    def derivative(self):
        # Computes the derivative of the polynomial
        if len(self.coefficients) <= 1:
            return Polynomial([0])
        return Polynomial([i * self.coefficients[i] for i in range(1, len(self.coefficients))])

    def __add__(self, other):
        # Adds two polynomials
        max_len = max(len(self.coefficients), len(other.coefficients))
        sum_coeffs = [0] * max_len
        for i in range(max_len):
            if i < len(self.coefficients):
                sum_coeffs[i] += self.coefficients[i]
            if i < len(other.coefficients):
                sum_coeffs[i] += other.coefficients[i]
        return Polynomial(sum_coeffs)

    def __mul__(self, other):
        # Multiplies two polynomials
        product_coeffs = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                product_coeffs[i + j] += self.coefficients[i] * other.coefficients[j]
        return Polynomial(product_coeffs)

# Example usage:
p1 = Polynomial([1, 2, 3])  # Represents 1 + 2x + 3x^2
p2 = Polynomial([3, 4])     # Represents 3 + 4x

print("P1: ", p1)
print("P2: ", p2)
print("P1 Degree: ", p1.degree())
print("P2 > P1: ", p2 > p1)
print("P1 Derivative: ", p1.derivative())
print("P1 + P2: ", p1 + p2)
print("P1 * P2: ", p1 * p2)
