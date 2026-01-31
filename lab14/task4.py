class Node:
    def __init__(self, coefficient=0, exponent=0, next=None):
        self.coefficient = coefficient
        self.exponent = exponent
        self.next = next

class Polynomial:
    def __init__(self):
        self.head = None

    def add_term(self, coefficient, exponent):
        new_node = Node(coefficient, exponent)
        if self.head is None or self.head.exponent < exponent:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.exponent > exponent:
                current = current.next
            if current.next and current.next.exponent == exponent:
                current.next.coefficient += coefficient
            else:
                new_node.next = current.next
                current.next = new_node

    def __add__(self, other):
        result = Polynomial()
        p1 = self.head
        p2 = other.head
        while p1 and p2:
            if p1.exponent > p2.exponent:
                result.add_term(p1.coefficient, p1.exponent)
                p1 = p1.next
            elif p1.exponent < p2.exponent:
                result.add_term(p2.coefficient, p2.exponent)
                p2 = p2.next
            else:
                result.add_term(p1.coefficient + p2.coefficient, p1.exponent)
                p1 = p1.next
                p2 = p2.next
        while p1:
            result.add_term(p1.coefficient, p1.exponent)
            p1 = p1.next
        while p2:
            result.add_term(p2.coefficient, p2.exponent)
            p2 = p2.next
        return result

    def __str__(self):
        result = ""
        current = self.head
        while current:
            if current.coefficient != 0:
                result += f"{current.coefficient}x^{current.exponent} "
                if current.next:
                    result += "+ "
            current = current.next
        return result.strip()

    def value(self, x):
        result = 0
        current = self.head
        while current:
            result += current.coefficient * (x ** current.exponent)
            current = current.next
        return result


p1 = Polynomial()
p1.add_term(4, 3)
p1.add_term(3, 2)
p1.add_term(2, 1)

p2 = Polynomial()
p2.add_term(1, 3)
p2.add_term(2, 2)
p2.add_term(3, 0)

print("Polynomial p1:", p1)
print("Polynomial p2:", p2)

p3 = p1 + p2
print("Sum of p1 and p2:", p3)

x_value = 2
print(f"Value of p1 at x={x_value}: {p1.value(x_value)}")
print(f"Value of p2 at x={x_value}: {p2.value(x_value)}")
print(f"Value of p3 at x={x_value}: {p3.value(x_value)}")