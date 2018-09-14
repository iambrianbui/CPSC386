class Point:
    def __init__(self, x, y, z):
        self.__x, self.__y, self.__z = x, y, z
        def getx(self): return self.__x
        def gety(self): return self.__y
        def getz(self): return self.__z

        def setx(self, x): self.__x = x
        def sety(self, y): self.__y = y
        def setz(self, z): self.__z = z

        x = property(getx, sety)
        y = property(gety, sety)
        z = property(getz, setz)

Point p(1,2,3)
print(p.x)
p,y = 12
print(p.y)