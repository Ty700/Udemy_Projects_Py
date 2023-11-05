class Animal():
    def __init__(self) -> None:
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale, Exhale")

#class Name(<class it inherits from>)

class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()
    
    def swim(self):
        print("Swimming in water")

    #Altering a method that a class inherited example:
    def breathe(self):
        # super().breath() - can leave this here if I want functionality of Animal's breathe() to happen.
        print("Inhale, Exhale in water")

Lion = Animal()
Lion.breathe()

nemo = Fish()
nemo.swim()
nemo.breathe() #gets this from Animal
print(f"{nemo.num_eyes}")