# Introduction of user defined type,
# here named Vector, a class
# __add__ member function, note it called as t+b, not as t.__add__(b) which it can be
# discussion of magic or dunder function members
# getters/setters (or accessor/mutators) instance members

class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.__x = x
        self.__y = y
        self.__z = z
        
    def __str__(self):
        vstr = "("
        vstr += str(self.__x)
        vstr += ", "
        vstr += str(self.__y)
        vstr += ", "
        vstr += str(self.__z)
        vstr += ")"
        return vstr
        
    def setX(self, d):    # required to assign a value to __x, especially outside the class
        self.__x = d
        return
    def getX(self):    # required to use __x, especially outside the class
        return self.__x
    def setY(self, d):
        self.__y = d
        return
    def getY(self):
        return self.__y
    def setZ(self, d):
        self.__z = d
        return
    def getZ(self):
        return self.__z
    
    def __add__(v1, v2):
        r = Vector()    # init called here
        r.__x = v1.__x+v2.__x
        r.__y = v1.__y+v2.__y
        r.__z = v1.__z+v2.__z
        return r

    def stp(v1, v2, v3):
        s = v1.__x * (v2.__y*v3.__z - v3.__y*v2.__z) - v1.__y * (v2.__x*v3.__z - v3.__x*v2.__z) + v1.__z * (v2.__x*v3.__y - v3.__x*v2.__y)
        return s
    staticmethod(stp)
    
def main():
    # t is 2i+j+5k
    t = Vector(2,1,5)    # init called here

    # m is 3i-2j+4k
    m = Vector(3,-2,4)    # init called here

    # b is 4i-j-2k
    b = Vector(4, -1, -2)    # init called here
    
    print(f"t: {t}")    # str called here
    print(f"m: {m}")    # str called here
    print(f"b: {b}")    # str called here

    # r is t+b
    r = t+b   # calling an instance dunder function
    print(f"t+b: {r}")    # str called here

    # s is stp ==>  t . m x b
    s = Vector.stp(t,m,b)   # calling a static member function
    print(f"stp: {s}")    # str called here
    
    print("=========================")
    print(f"t.x: {t.getX()}")
    r.setZ(-9)
    print(f"(t+b).z: {r.getZ()}")
    print("=========================")
    
main()