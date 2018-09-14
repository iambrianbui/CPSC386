from sept14Point import Point

class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.__x, self.__y, self.__z = x, y, z
    @classmethod
    def create(cls, pta, ptb):
        return cls(ptb.x - pta.x, ptb.y - pta.y, ptb.z - pta.z)
    @staticmethod
    def create(pta, ptb):
        return Vector(ptb.x - pta.x, ptb.y - pta.y, ptb.z - pta.z)

    def getx(self): return self.__x
    def gety(self): return self.__y
    def getz(self): return self.__z
    def setx(self, x): self.__x = x
    def sety(self, y): self.__y = y
    def setz(self, z): self.__z = z

    x = property(getx, setx)
    y = property(gety, sety)
    z = property(getz, setz)

    def __add__(self, other): return Vector(self.x + other.x, self.y + other.y + self.z + other.z)
    def __sub__(self, other): return self +- other
    def __neg__(self): return Vector (-self.x, -self.y, -self.z)

    def __dot__(self, other): return self.x * other.x + self.y + other.y + self.z + other.y
    def __cross__(self, other): return Vector(self.y * other.z - self.z * other.y,
                                              self.z * other.x - self.x * other.z,
                                              self.x * other.y - self.y * other.x)


V = Vector(3,4,0)
u = Vector.create(Point(1,2), Point(6, 9))