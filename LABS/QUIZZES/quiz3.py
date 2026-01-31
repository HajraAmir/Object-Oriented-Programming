class Polynomial:
    def __init__(self, coeffs):
        # coeffs should be a list of coefficients, e.g., [1, 2, 3] for 1 + 2x + 3x^2.
        self.coeffs = coeffs

    def __getitem__(self, index):
        # Allows getting a coefficient using p[index].
        return self.coeffs[index]

    def __setitem__(self, index, value):
        # Allows setting a coefficient using p[index] = value.
        self.coeffs[index] = value

    def __gt__(self, other):
        # Checks if the degree of this polynomial is greater than another.
        # The degree is the highest power of x, which corresponds to the length of coeffs list - 1.
        return len(self.coeffs) > len(other.coeffs)

    def derivative(self):
        # Returns the derivative of the polynomial.
        if len(self.coeffs) == 1:
            # The derivative of a constant is 0.
            return Polynomial([0])
        else:
            # The derivative of ax^n is n*ax^(n-1).
            return Polynomial([i * self.coeffs[i] for i in range(1, len(self.coeffs))])

    def __add__(self, other):
        # Adds this polynomial to another.
        max_len = max(len(self.coeffs), len(other.coeffs))
        sum_coeffs = [0] * max_len
        for i in range(max_len):
            if i < len(self.coeffs):
                sum_coeffs[i] += self.coeffs[i]
            if i < len(other.coeffs):
                sum_coeffs[i] += other.coeffs[i]
        return Polynomial(sum_coeffs)

    def __mul__(self, other):
        # Multiplies this polynomial by another.
        result_coeffs = [0] * (len(self.coeffs) + len(other.coeffs) - 1)
        for i in range(len(self.coeffs)):
            for j in range(len(other.coeffs)):
                result_coeffs[i + j] += self.coeffs[i] * other.coeffs[j]
        return Polynomial(result_coeffs)

# Example usage:
p1 = Polynomial([1, 2, 3])  # Represents 1 + 2x + 3x^2
p2 = Polynomial([3, 4])     # Represents 3 + 4x

# Access and modify coefficients
print("Coefficient at position 1 of p1:", p1[1])
p1[1] = 5
print("Modified p1:", p1.coeffs)

# Degree comparison
print("p1 is bigger than p2:", p1 > p2)

# Derivative
print("Derivative of p1:", p1.derivative().coeffs)

# Addition
print("Sum of p1 and p2:", (p1 + p2).coeffs)

# Multiplication
print("Product of p1 and p2:", (p1 * p2).coeffs)
