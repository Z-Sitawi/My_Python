class Date:
    def __init__(self, d, m, y):
        self.day = d
        self.month = m
        self.year = y

    def __str__(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year:04d}"


class Person:
    def __init__(self, n, c, date_of_birth):
        self.name = n
        self.city = c
        self.date_of_birth = date_of_birth

    def age(self, current_year):
        return current_year - self.date_of_birth.year

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Day of Birth: {self.date_of_birth}\n"
            f"City of Birth: {self.city}\n"
            f"Age: {self.age(2023)}"
        )


dob = Date(14, 1, 2003)
s = Person("Zakaria", "Rabat", dob)
print(s.age(2083))