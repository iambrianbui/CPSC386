import math
from sept14Point import Point
from sept14vector import Vector


class Triangle:

    def __init__(self, a, b, c):
        self.__a, self.__b, self.__c = a, b, c

    def geta(self): return self.__a
    def getb(self): return self.__b
    def getc(self): return self.__c

    def seta(self): return self.__a
    def setb(self): return self.__b
    def setc(self): return self.__c

    a = property(geta, seta)
    b = property(getb, setb)
    c = property(getc, setc)

    def getab(self): return math.sqrt(pow(self.__a.x() - self.__b.x(), 2) + pow(self.__a.y() - self.__b.y(), 2))
    def getbc(self): return math.sqrt(pow(self.__b.x() - self.__c.x(), 2) + pow(self.__b.y() - self.__c.y(), 2))
    def getac(self): return math.sqrt(pow(self.__a.x() - self.__c.x(), 2) + pow(self.__a.y() - self.__c.y(), 2))

    ab = property(getab)
    bc = property(getbc)
    ac = property(getac)


   # def __collision__(self, other):