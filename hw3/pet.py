class Pet():
    species = {
        "cat": 16,
        "dog": 14,
        "bird": 8,
    }

    def __init__(self, name, age, petSpecies):
        self.name = name
        self.age = age
        self.petSpecies = petSpecies

    def human_years(self):
        return self.age * 7

    def average_lifespan(self, species):
        return self.species[species]

pet1 = Pet("Catsy", 14, "cat")
pet2 = Pet("Cosmo", 8, "dog")
pet3 = Pet("Bella", 5, "bird")

print(pet1.name, "human age:", pet1.human_years())
print(pet1.name, "average lifespan:", pet1.average_lifespan(pet1.petSpecies))

print(pet2.name, "human age:", pet2.human_years())
print(pet2.name, "average lifespan:", pet2.average_lifespan(pet2.petSpecies))

print(pet3.name, "human age:", pet3.human_years())
print(pet3.name, "average lifespan:", pet3.average_lifespan(pet3.petSpecies))
