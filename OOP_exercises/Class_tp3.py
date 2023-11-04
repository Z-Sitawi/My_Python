class Employe:
    """this is a comment!"""
    def __init__(self, nom, prenom, date_de_naissance, saliare, b=250):
        self.__nom = nom
        self.__pre = prenom
        self.__dn = date_de_naissance
        self.__saliare = saliare
        self.bonus = b

    def affichier(self):
        print("___________________________________________________________")
        print(f"Nom: {self.__nom}\nPrenom: {self.__pre}\n"
              f"Date de Naissance: {self.__dn}\nSaliare: {self.__saliare} MAD")
        print("___________________________________________________________")

    def getinfo(self, e=str()):
        e = e.lower()
        if e == "nom":
            return self.__nom
        elif e == "prenom":
            return self.__pre
        elif e == "dn":
            return self.__dn
        elif e == "saliare":
            return self.__saliare
        else:
            return "error"

    def setinfo(self, a, e=str()):
        e = e.lower()
        if e == "nom":
            self.__nom = a
        elif e == "prenom":
            self.__pre = a
        elif e == "dn":
            self.__dn = a
        elif e == "salaire":
            self.__saliare = a
        else:
            return "error"

    def getlastname(self):
        return self.__nom

    def setlastname(self, lastname):
        self.__nom = lastname

    def getname(self):
        return self.__pre

    def setname(self, name):
        self.__pre = name

    def getdn(self):
        return self.__dn

    def setdn(self, date):
        self.__dn = date

    def getsalaire(self):
        return self.__saliare

    def setsalaire(self, salaire):
        self.__saliare = salaire

    def cal_sal(self):
        total = self.__saliare + self.bonus
        return total

    def __str__(self):
        return (f"Nom: {self.__nom}\nPrenom: {self.__pre}\nDate de Naissance: {self.__dn}"
                f"\nSaliare: {self.__saliare} MAD\nBonus: {self.bonus} MAD\nTotal S: {self.cal_sal()} MAD\n\n")


x = Employe("Ben Jaloun", "Hassan", "20/12/1990", 5000)

print(x)

