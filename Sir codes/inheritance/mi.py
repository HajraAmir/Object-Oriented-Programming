class Parent1:
    def __init__(self, name):
        print("Parent1 init")
        self.name = name
    def greet1(self):
        print(f"Parent1: Hello, {self.name}")

class Parent2:
    def __init__(self, age):
        print("Parent2 init")
        self.age = age
    def greet2(self):
        print(f"Parent2: Hello, I'm {self.age} years old")

class Parent3:
    def __init__(self, gndr):
        print("Parent3 init")
        self.gender = gndr
    def greet3(self):
        print(f"Parent3: Hello, I'm a {self.gender}")

class Child(Parent1, Parent2, Parent3):
    def __init__(self, name, age):
        print("Child init")
        super().__init__(name)
        #super(Child, self).__init__(name)
        super(Parent1, self).__init__(age)
        super(Parent2, self).__init__('male')

child = Child("Alice", 10)
child.greet1()
child.greet2()
child.greet3()
print()
print(child.name)
print(child.age)
print(child.gender)
print()
print(Child.mro())
print(Parent1.mro())

