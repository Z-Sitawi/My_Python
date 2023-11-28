from math import sqrt


class Point:
    nb = 0

    def __init__(self, x, y):
        self.__abs = x
        self.__ord = y
        Point.nb = Point.nb + 1

    @property
    def abs(self):
        return self.__abs

    @abs.setter
    def abs(self,  x):
        self.__abs = x

    @property
    def ord(self):
        return self.__ord

    @ord.setter
    def ord(self, y):
        self.__ord = y

    def __str__(self):
        return f"Point({self.__abs}, {self.__ord})\n"

    def calculermilieu(self, p):
        mx = (self.__abs + p.__abs) / 2
        my = (self.__ord + p.__ord) / 2
        mp = Point(mx, my)
        return mp

    def __pow__(self, power, modulo=None):
        x = self.__abs ** power.__abs
        y = self.__ord ** power.__ord
        return Point(x, y)

    def __lt__(self, p):
        m_self = sqrt((self.__abs ** 2) + (self.__ord ** 2))
        m2_p = sqrt((p.__ord ** 2) + (p.__ord ** 2))
        return m_self < m2_p


a = Point(2, 4)
b = Point(2, 2)
m = a.calculermilieu(b)
print("a = ", a, "b = ", b, "a ** b = ", a ** b, sep='')
print(a < b)