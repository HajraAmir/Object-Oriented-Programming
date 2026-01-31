class GP:
    def __init__(self, spr):
        print("GP init")
        self.spr_name = spr
    def greet(self):
        print(f"GP: Hello, {self.spr_name}")

class Parent1(GP):
    def __init__(self, name, x):
        print("Parent1 init")
        #super(Parent3, self).__init__(x)
        self.name = name
    def greet1(self):
        print(f"Parent1: Hello, {self.name}")

class Parent2(GP):
    def __init__(self, age, y):
        print("Parent2 init")
        #super(Parent3, self).__init__(y)
        self.age = age
    def greet2(self):
        print(f"Parent2: Hello, I'm {self.age} years old")

class Parent3(GP):
    def __init__(self, gndr, z):
        print("Parent3 init")
        #super(Parent3, self).__init__(z)
        super().__init__(z)
        self.gender = gndr
    def greet3(self):
        print(f"Parent3: Hello, I'm a {self.gender}")

class Child(Parent1, Parent2, Parent3):
    def __init__(self, name, age, gndr, a):
        print("Child init")
        super().__init__(name, a)
        super(Parent1, self).__init__(age, a)
        super(Parent2, self).__init__(gndr, a)

child = Child("Alice", 10, 'female', 'top')
child.greet()
child.greet1()
child.greet2()
child.greet3()

print(child.spr_name)
print(child.name)
print(child.age)
print(child.gender)

print(Child.mro())
print(Parent1.mro())

