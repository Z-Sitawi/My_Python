from abc import *


class Vehicle(ABC):
    matric = 10000

    def __init__(self, model, prix):
        self._matricule = Vehicle.matric
        Vehicle.matric = Vehicle.matric + 100
        self._model = model
        self._prix = prix

    @property
    def matricule(self):
        return self._matricule

    @matricule.setter
    def matricule(self, matricule):
        self._matricule = matricule

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

    @property
    def prix(self):
        return self._prix

    @prix.setter
    def prix(self, prix):
        self._prix = prix

    def demarrer(self):
        pass

    def accelerer(self):
        pass

    def __str__(self):
        return (f"Matricule: {self.matricule}\nModel: {self.model}\nPrix: {self.prix} $\n"
                f"Demmarer: {self.demarrer()}\nAccelerer: {self.accelerer()}")


class Car(Vehicle):
    def __init__(self, model, prix):
        Vehicle.__init__(self, model, prix)

    def demarrer(self):
        return f"This is Method demarer() For car: {self.matricule}"

    def accelerer(self):
        return f"This is Method accelerer() For car: {self.matricule}"


class Truck(Vehicle):
    def __init__(self, model, prix):
        Vehicle.__init__(self, model, prix)

    def demarrer(self):
        return f"This is Method demarer() For Truck: {self.matricule}"

    def accelerer(self):
        return f"This is Method accelerer() For Truck: {self.matricule}"


car1 = Car(2003, 50000)
car1.prix = 900000
car2 = Car(2000, 800000)
t1 = Truck(2015, 800000)
t2 = Truck(1999, 855000)

print(car1, car2, t1, t2, sep="\n---------------\n")