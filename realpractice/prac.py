class Person:
    def __init__(self,name):
        self.name = name

    def SayHello(self):
        print('Hello, my name is ' + self.name)

    def __del__(self):
        print('%s says bye.' % self.name)


B = Person('Brian Bui')


class Point:
    def __init__(self, size, length):
        self.size = size
        # private
        self.__length = length
    def __str__(self):
        print('A(size=' + str(self.size) +
              ' , length=' + str(self.__length) + ')')
    def length(self): return self.__length
    def size(self): return self.size


a = Point(10, 20)
a.size
a.length



