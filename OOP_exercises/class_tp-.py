class Etudiant:
    def __init__(self, name, all_notes):
        self._name = name
        if not isinstance(all_notes, list):
            raise ValueError("last argument must be a list")
        all(all_notes)
        print("both value and index must be int")

    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, value, idx):
        try:
            self._notes[idx] = value
        except ValueError:
            print("both value and index must be int")
        except IndexError:
            print(f"Index out of range: [0: {len(self._notes) - 1}")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, nn):
        self._name = nn

    def clc_moy(self):
        """ calculer la moyenne """
        some = 0
        for x in self._notes:
            some = some + x
        return some / len(self._notes)

    def __str__(self):
        return f"La moyeene = {self.clc_moy()}"


s = Etudiant("zak", [19, 20])
print(s)