class Persone:
    def __init__(self, name, cin, bth):
        self._name = name
        self._cin = cin
        self._bth = bth

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        self._name = n

    @property
    def cin(self):
        return self._cin

    @cin.setter
    def cin(self, cin):
        self._cin = cin

    @property
    def bth(self):
        return self._bth

    @bth.setter
    def bth(self, bth):
        self._bth = bth

    def age(self):
        return 2023 - self._bth

    def afficher(self):
        print(f"Name: {self._name}\nCIN: {self._cin}\nBirth Day: {self._bth}\nAge: {self.age()} years old.")


class Etudiant(Persone):
    def __init__(self, name, cin, bth, note1, note2):
        Persone.__init__(self, name, cin, bth)
        self._note1 = note1
        self._note2 = note2

    @property
    def note1(self):
        return self._note1

    @note1.setter
    def note1(self, nn):
        self._note1 = nn

    @property
    def note2(self):
        return self._note2

    @note2.setter
    def note2(self, nn):
        self._note2 = nn

    def afficher(self):
        Persone.afficher(self)
        print(f"Note 1 = {self._note1}\nNote 2 = {self._note2}")


class Employee(Persone):
    def __init__(self, name, cin, bth, ph, nbrh):
        Persone.__init__(self, name, cin, bth)
        self.prixheure = ph
        self.nbrheure = nbrh

    def salaire(self):
        return self.nbrheure * self.prixheure

    def afficher(self):
        Persone.afficher(self)
        print(f"Prix Heure: {self.prixheure}\nNbr Heure: {self.nbrheure}\nSalaire: {self.salaire()}")


a = Persone("Zakaria", 555555, 2003)
b = Etudiant("Zakaria", 555555, 2003, 15, 20)
c = Employee("Zakaria", 555555, 2003, 100, 40)
print("_______________________Person______________________________")
a.afficher()
print("_______________________Etudiant_____________________________")
b.afficher()
print("_______________________Employee_____________________________")
c.afficher()