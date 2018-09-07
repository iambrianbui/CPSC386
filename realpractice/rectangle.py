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


class Rectangle:

    #  in this case, length will be the fixed x distance
    def __init__(self, upperleft, bottomright):
        self.__upperleft = upperleft
        self.__bottomright = bottomright

    def upperleft(self): return self.__upperleft

    def bottomright(self): return self.__bottomright

    def upperright(self): return Point(self.__bottomright.x(), self.__upperleft.y())

    def bottomleft(self): return Point(self.__upperleft.x(), self.__bottomright.y())

    def __deltax_deltay(self):
        delx = self.upperright().x() - self.upperleft().x()
        dely = self.bottomleft().y() - self.upperleft().y()
        return delx, dely

    def length(self):
        dxdy = self.__deltax_deltay()
        return dxdy[0] if dxdy[0] > dxdy[1] else dxdy[1]

    def width(self):
        dxdy = self.__deltax_deltay()
        return dxdy[1] if dxdy[0] > dxdy[1] else dxdy[0]

    def area(self):
        return self.length() * self.width()

    def perimeter(self):
        return (2 * self.length()) + (2 * self.width())

    def __str__(self):
        return ' Upper Right:  ' + str(self.upperright()) + '\n Upper Left:  ' + str(self.upperleft()) + \
               '\n Bottom Right:  ' + str(self.bottomright()) + '\n Bottom Left:  ' + str(self.bottomleft()) + \
               '\n Length:  ' + str(self.length()) + '\n Width:  ' + str(self.width()) + \
               '\n Area:  ' + str(self.area()) + '\n Perimeter:  ' + str(self.perimeter())

