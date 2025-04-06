# Superhero class (parent class)
class Superhero:
    def __init__(self, name, superpower):
        self.name = name
        self.superpower = superpower

    def introduce(self):
        print(f"I am {self.name}, and I have the power of {self.superpower}!")

    def perform_action(self):
        print(f"{self.name} is saving the day!")

# Inheritance: FlyingHero class (child class)
class FlyingHero(Superhero):
    def __init__(self, name):
        super().__init__(name, "flight")
    
    def perform_action(self):
        print(f"{self.name} is flying high to the rescue!")

# Inheritance: SuperStrengthHero class (child class)
class SuperStrengthHero(Superhero):
    def __init__(self, name):
        super().__init__(name, "super strength")
    
    def perform_action(self):
        print(f"{self.name} is lifting massive objects to save the day!")

# Create superhero objects
hero1 = FlyingHero("SkyMaster")
hero2 = SuperStrengthHero("StrengthMan")

# Call methods
hero1.introduce()
hero1.perform_action()  

hero2.introduce()
hero2.perform_action()  