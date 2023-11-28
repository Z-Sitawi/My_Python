class CompteBancaire:
    def __init__(self, numerocompte, nom, solde):
        self.nc = numerocompte
        self.name = nom
        self.balance = solde

    def versement(self, versement):
        self.balance = self.balance + versement

    def retrait(self, retrait):
        if retrait <= self.balance:
            self.balance = self.balance - retrait
        else:
            self.balance = self.balance - (retrait * 0)

    def agios(self):
        self.balance = self.balance * 0.95

    def affichier(self):
        print(f"Numero du Compte: {self.nc}\nNom du Client: {self.name}\nSolde: {self.balance:.2f}\n")


c1 = CompteBancaire(123456789, "Taha", 120.50)
c2 = CompteBancaire(757575757, "Badr", 1)