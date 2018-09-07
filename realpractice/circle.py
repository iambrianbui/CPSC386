import math


class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return 'Point(' + str(self.__x) + ', ' + str(self.__y) + ') '

    def x(self): return self.__x

    def y(self): return self.__y

    def distance(self, other):
        delx = self.__x - other.__x
        dely = self.__y - other.__y
        return math.sqrt(delx ** 2 + dely ** 2)


class Circle:

    def __init__(self, radius, center):
        self.__radius, self.__center = radius, center

    def radius(self): return self.__radius

    def center(self): return self.__center

    def area(self): return math.pi * self.__radius ** 2

    def perimeter(self): return 2 * math.pi * self.__radius

    def distance(self, other): return self.__center.distance(other.__center)

    def collision(self, other):
        combinedRadius = self.__radius + other.__radius
        centerDistance = self.distance(other)
        return combinedRadius > centerDistance



p = Point(1, 1)
str(p)
q = Point(4, 1)
str(q)
p.distance(q)

c1 = Circle(2, Point(1,1))
c2 = Circle(4, Point(2,2))
print(str(c1.collision(c2)))
