class parent(object):
    def __init__(self):
        print("base init called")
        self.dm1 = "base data member 1"
        self.dm2 = "base data member 2"
        
class child(parent):
    def __init__(self):
        super().__init__()
        print("child init called")
        self.dm3 = "child data member 3"
        self.dm4 = "child data member 4"
       
def main():
    p = parent()
    # parent object p has two data members defined in it
    print(p.dm1)
    print(p.dm2)
    c = child()
    # child object c has four data members, two defined in it and two from its base classes
    print(c.dm1)
    print(c.dm2)
    print(c.dm3)
    print(c.dm4)

main()     