class polynomial:
    def __init__(p, degree):
        #p=polynomial()
        p.degree=degree
        p.cofficient=[0]*(p.degree+1)
        p.variable='x'
        #return p
    #staticmethod(creatpolynomial)
    def setcofficient(p,degree,cofficient):
        p.cofficient[degree]=cofficient
        return p
    #staticmethod(setcofficient)
    def printpolynomial(p):
        i=p.degree
        while i>=0:
            print(p.cofficient[i],end='')
            print(p.variable,end='')
            print('^',end='')
            if i!=0:
                print(i,end='+')
            else:
                print(i,end=' ')
            i=i-1
    #staticmethod(printpolynomial)
    def addpolynomial(p1,p2):
        #   add some degree in call below
        p3=polynomial(4)

        #if p1.degree>p2.degree:
        #    p3.degree=p1.degree
        #else:p3.degree=p2.degree
        #p3.cofficient=[0]*(p3.degree+1)
        #p3.variable=p1.variable
        i=p3.degree
        while i>0:
           p3.setcofficient(i,p1.cofficient[i]+p2.cofficient[i])
           i=i-1
        return p3
    #staticmethod(addpolynomial)

degree=4
e=polynomial(degree)
e.setcofficient(4, -2)
e.setcofficient(3, -2)
e.setcofficient(2, 5)
e.setcofficient(1, 5)
e.setcofficient(0, 1)
degree=4
g=polynomial(degree)
g.setcofficient(3, 43)
g.setcofficient(2, 10)
g.setcofficient(1, 2)
g.setcofficient(0, 1)
f=e.addpolynomial(g)
f.printpolynomial()