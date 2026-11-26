class character:
    def __init__(self,name,health):
        self.name = name
        self.health = health
    def attack(self):
        print(f"{self.name}attacks!")

class warrior(character):
    def __init__(self,name,health):
        super().__init__(name,health)
    def attack(self):
        print(self.name,"attact with sword!")

class mage(character):
    def __init__(self,name,health):
        super().__init__(name,health)

    def attack(self):
        print(self.name,"attacks with magic!")

class archer(character):
    def __init__(self,name,health):
        super().__init__(name,health)


    def attack(self):
        print(self.name,"attack with arrow!")

warrior = warrior("Thor",100)
mage = mage("melin",80)
archer = archer("robin",90)

characters = [warrior,mage,archer]

for character in characters:
    character.attack()