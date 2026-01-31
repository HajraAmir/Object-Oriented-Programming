class Matrix:
    def __init__(self, rows, cols, initial_value=0):
        self.rows = rows
        self.cols = cols
        self.data = [[initial_value for _ in range(cols)] for _ in range(rows)]

    def __repr__(self):
        result = ""
        for row in self.data:
            result += " ".join(map(str, row)) + "\n"
        return result.strip()

    def set_element(self, row, col, value):
        self.data[row][col] = value

    def get_element(self, row, col):
        return self.data[row][col]

    def add(self, other):
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def subtract(self, other):
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result

    def multiply(self, other):
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

    def transpose(self):
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[j][i] = self.data[i][j]
        return result
# Create a 2x2 matrix
matrix1 = Matrix(2, 2)
matrix1.set_element(0, 0, 1)
matrix1.set_element(0, 1, 2)
matrix1.set_element(1, 0, 3)
matrix1.set_element(1, 1, 4)

# Create another 2x2 matrix
matrix2 = Matrix(2, 2)
matrix2.set_element(0, 0, 5)
matrix2.set_element(0, 1, 6)
matrix2.set_element(1, 0, 7)
matrix2.set_element(1, 1, 8)

# Print matrices
print("Matrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)

# Add matrices
result_add = matrix1.add(matrix2)
print("\nAddition of Matrix 1 and Matrix 2:")
print(result_add)

# Subtract matrices
result_subtract = matrix1.subtract(matrix2)
print("\nSubtraction of Matrix 1 and Matrix 2:")
print(result_subtract)

# Create a 2x3 matrix and a 3x2 matrix for multiplication
matrix3 = Matrix(2, 3)
matrix3.set_element(0, 0, 1)
matrix3.set_element(0, 1, 2)
matrix3.set_element(0, 2, 3)
matrix3.set_element(1, 0, 4)
matrix3.set_element(1, 1, 5)
matrix3.set_element(1, 2, 6)

matrix4 = Matrix(3, 2)
matrix4.set_element(0, 0, 7)
matrix4.set_element(0, 1, 8)
matrix4.set_element(1, 0, 9)
matrix4.set_element(1, 1, 10)
matrix4.set_element(2, 0, 11)
matrix4.set_element(2, 1, 12)

# Multiply matrices
result_multiply = matrix3.multiply(matrix4)
print("\nMultiplication of Matrix 3 and Matrix 4:")
print(result_multiply)

# Transpose matrix
result_transpose = matrix1.transpose()
print("\nTranspose of Matrix 1:")
print(result_transpose)
