class Vector4d:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def magnitude_squared(self):
        return self.x**2 + self.y**2 + self.z**2 + self.w**2

    def is_unit_vector(self):
        return self.magnitude_squared() == 1

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z + self.w * other.w

    def difference(self, other):
        return Vector4d(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)

    def additive_inverse(self):
        return Vector4d(-self.x, -self.y, -self.z, -self.w)

    def __repr__(self):
        return f"Vector4d({self.x}, {self.y}, {self.z}, {self.w})"

v1 = Vector4d(1, 2, 3, 4)
v2 = Vector4d(2, 3, 4, 5)

print("Magnitude of v1 squared:", v1.magnitude_squared())
print("Is v1 a unit vector?", v1.is_unit_vector())

print("Dot product of v1 and v2:", v1.dot_product(v2))
print("Difference of v1 from v2:", v1.difference(v2))
print("Additive inverse of v1:", v1.additive_inverse())
