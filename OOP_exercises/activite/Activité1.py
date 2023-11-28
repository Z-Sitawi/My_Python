import math


class Point:
    """ difiner une point"""
    nb = 0

    def __init__(self, x, y):
        self.__abs = x
        self.__ord = y
        Point.nb += 1

    @property
    def abs(self):
        return self.__abs

    @abs.setter
    def abs(self, x):
        self.__abs = x

    @property
    def ord(self):
        return self.__ord

    @ord.setter
    def ord(self, y):
        self.__ord = y

    def __str__(self):
        """ retourne la représentation mathématique d’un point :
            (abs,ord)
        """
        return f"({self.__abs}, {self.__ord})"

    def __eq__(self, other):
        """
        permettant de vérifiant si deux point p1(x1,y1)
        et p2(x2,Y2) sont égaux ou non(x1=x2 et y1=y2)

        :param other: la deuxéme point
        :return: égaux ou pas égaux
        """
        if self.__abs == other.abs and self.__ord == other.ord:
            return f"les duex point sont égaux"
        else:
            return f"les duex point sont pas égaux"

    def calculerdistance(self, p):
        """
        Permet de calculer la distance entre le point
        de l’objet courant (self) et l’objet p

        :param p: la deuxéme point
        :return: la distance

        """
        x = self.abs - p.abs
        y = self.ord - p.ord
        distance = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
        # print(f"la distance entre les deux point = {round(distance)}")
        return distance

    def calculermilieu(self, p):
        """
        permet de calculer abs et ord du point au milieu de
        self et p

        :param p: l’objet 2 éme Point
        :return: un objet correspondant au milieu
        """
        mx = (self.abs + p.abs) / 2
        my = (self.ord + p.ord) / 2
        mp = Point(round(mx, 2), round(my, 2))
        return mp


class TroisPoints:
    def __init__(self, p1, p2, p3):
        self.__point1 = Point(p1.abs, p1.ord)
        self.__point2 = Point(p2.abs, p2.ord)
        self.__point3 = Point(p3.abs, p3.ord)

    @property
    def point1(self):
        return self.__point1

    @point1.setter
    def point1(self, p1):
        self.__point1 = Point(p1.ord, p1.abs)

    @property
    def point2(self):
        return self.__point2

    @point2.setter
    def point2(self, p2):
        self.__point2 = Point(p2.ord, p2.abs)

    @property
    def point3(self):
        return self.__point3

    @point3.setter
    def point3(self, p3):
        self.__point3 = Point(p3.ord, p3.abs)

    def __str__(self):
        return (f"p1{self.point1.abs, self.point1.ord}\n"
                f"p2{self.point2.abs, self.point2.ord}\n"
                f"p3{self.point3.abs, self.point3.ord}\n")

    def sontalignes(self):
        """
            return True si les trois points point1 , point2 et point3 sont alignés, False sinon.
            Nous rappelons que trois points A, B et C sont alignés
            si AB = AC + BC ou AC = AB + BC ou BC = AC + AB
            (AB désignant la distance séparant le point A du point B, pareillement pour AC et BC).
        """
        AB = self.point1.calculerdistance(self.point2)
        AC = self.point1.calculerdistance(self.point3)
        BC = self.point2.calculerdistance(self.point3)

        if AB == AC + BC or AC == AB + BC or BC == AC + AB:
            return True
        else:
            return False

    def estisocele(self):
        """

        return: True si les trois points point1, point2 et point3
                forment un triangle isocèle False sinon.

        Nous rappelons qu’un triangle ABC est isocèle si AB = AC ou AB = BC ou BC = AC.

        """
        AB = self.point1.calculerdistance(self.point2)
        AC = self.point1.calculerdistance(self.point3)
        BC = self.point2.calculerdistance(self.point3)

        if self.sontalignes():
            return 100
        else:
            if AB == AC or AB == BC or BC == AC:
                return True
            else:
                return False

    @staticmethod
    def calculerdistance(p1, p2):
        """
                Permet de calculer la distance entre les deux point p1 et p2

                :param p1: la premier point
                :param p2: la deuxéme point
                :return: la distance entre les deux point

                """
        return math.sqrt(math.pow(p1.abs - p2.abs, 2) + math.pow(p1.ord - p2.ord, 2))

    @staticmethod
    def calculermilieu(p1, p2):
        """
        permet de calculer abs et ord du point au milieu de
        p1 et p2

        :param p1: la premier point
        :param p2: la deuxéme point
        :return: point au milieu de p1 et p2

        """
        xM = (p1.abs + p2.abs) / 2
        yM = (p1.ord + p2.ord) / 2
        return Point(xM, yM)
