class Employe:

    def __init__(self, matr, nom, prenom, date_de_naissance, date_embauche, saliare):
        self.matricule = matr
        self.nom = nom
        self.pre = prenom
        self.dn = date_de_naissance
        self.de = date_embauche
        self.saliare = saliare

    def age(self):
        return 2023 - self.dn

    def anciennete(self):
        return 2023 - self.de

    def augmentation_du_salaire(self):
        ans = self.anciennete()
        if ans < 5:
            self.saliare = self.saliare + (self.saliare * 0.02)
        elif ans < 10:
            self.saliare = self.saliare + (self.saliare * 0.05)

        else:
            self.saliare = self.saliare + (self.saliare * 0.1)

    def __str__(self):
        return (f"\n______________________________________________________________________________\n"
                f"Matricule: {self.matricule}\nNom: {self.nom}\nPrénom: {self.pre}\n "
                f"Date de Nissance: {self.dn}\nDate Embauche: {self.de}\nanciennete: {self.anciennete()}\n"
                f"Age: {self.age()}\nSalaire: {self.saliare} MAD")


e1 = Employe("AZ482514", "Zakaria", "Aaichaou", 1989, 2010, 5000)
e2 = Employe("AD329063", "Hoda", "Frirra", 2000, 2020, 5000)
e3 = Employe("A0801543", "Badr", "Hossa", 1984, 2015, 5000)

e1.augmentation_du_salaire()
e2.augmentation_du_salaire()
e3.augmentation_du_salaire()

print(e1, e2, e3)