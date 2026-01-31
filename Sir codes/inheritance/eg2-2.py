class shape:    # implicitly inherits python builtin 'object' class
    def __init__(self, nam, ol, bc):
        self.name = nam
        self.outline = ol
        self.background = bc
    def __str__(self):
        return f"{self.name}, {self.outline}, {self.background}"

class square(shape):
    def __init__(self, nam, ol, bc, sl):
        super().__init__(nam, ol, bc)
        self.length = sl
    def __str__(self):
        return f"{super().__str__()}, {self.length}"
    def area(self):
        return self.length ** 2

class rectangle(square):
    def __init__(self, nam, ol, bc, ln, wd):
        # below is another way to call super()
        square.__init__(self, nam, ol, bc, ln)
        self.width = wd
    def __str__(self):
        # below is another way to call super()
        return f"{square.__str__(self)}, {self.width}"
    def area(self):
        return self.length * self.width

def main():
    s = shape('sh1', True, 'yellow')
    print(s)
    sqr = square('sq1', False, 'golden', 7)
    print(sqr)
    print("Area", sqr.area())
    rtg = rectangle('rg1', True, 'blue', 12, 13)
    print(rtg)
    print("Area", rtg.area())


main()
