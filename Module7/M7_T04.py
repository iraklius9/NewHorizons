import math


class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def distance(self, other):
        return math.hypot(self.__x - other.__x, self.__y - other.__y)


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        return self.__vertices[0].distance(self.__vertices[1]) + self.__vertices[1].distance(self.__vertices[2]) + \
            self.__vertices[2].distance(self.__vertices[0])


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
