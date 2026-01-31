class Pet:
    def _init_(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def get_name(self):
        self.name

    def get_species(self):
        return self.species
    def get_age(self):
        return self.age
    def set_name(self,name):
        self.name=name
    def set_species(self,species):
        self.species=species
    def set_age(self,age):
        self.age=age        
def main():
        
    pet1 = Pet("Fluffy", "Cat", 3)
    pet2 = Pet("Buddy", "Dog", 5)

    print(pet1.get_age())
    print(pet1.get_name())

    print(pet1.get_species())  
    print(pet2.get_species())  