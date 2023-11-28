class Rectangle:
    def __init__(self, lon, lar):
        self._longueur = lon
        self._largeur = lar

    def perimetre(self):
        return (self._largeur + self._longueur) * 2

    def surface(self):
        return self._largeur * self._longueur

    @property
    def lon(self):
        return self._longueur

    @lon.setter
    def lon(self, lon):
        self._longueur = lon

    @property
    def lar(self):
        return self._largeur

    @lar.setter
    def lar(self, lar):
        self._largeur = lar

    def __str__(self):
        return (f"___________________________________________________________________\n"
                f"Longueur = {self.lon} m\nLargeur = {self.lar} m\n"
                f"Perimetre = {self.perimetre()} m\nSurface = {self.surface()}\n"
                f"___________________________________________________________________\n")


class Parallelepipede(Rectangle):
    def __init__(self, lon, lar, h):
        Rectangle.__init__(self, lon, lar)
        self._hauteur = h

    @property
    def hau(self):
        return self._hauteur

    @hau.setter
    def hau(self, h):
        self._hauteur = h

    def volume(self):
        return self.lon * self.lar * self._hauteur

    def __str__(self):
        return (f"___________________________________________________________________\n"
                f"Longueur = {self.lon} m\nLargeur = {self.lar} m\nHauteur = {self._hauteur} m\n"
                f"Perimetre = {self.perimetre()} m\nSurface = {self.surface()} m²\nVolume = {self.volume()} m*m²\n"
                f"___________________________________________________________________\n")


a = Rectangle(5, 2)
o = Parallelepipede(a.lon, a.lar, 3)
print(a)
print(o)