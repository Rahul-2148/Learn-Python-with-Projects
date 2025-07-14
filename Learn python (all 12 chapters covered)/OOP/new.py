class Character:
    def __init__(self, name, health, attack, blood):
        self.name = name
        self.health = health
        self.attack = attack
        self.blood = blood

    def attack_enemy(self):
        print(f"{self.name} attacks with power {self.attack} and {self.blood} blood")

warrior = Character('Thor', 100, 50, 'red')
mage = Character('Gandalf', 80, 70, 'black')
archer = Character('Archer', 80, 90, 'white')

warrior.attack_enemy()
mage.attack_enemy()
archer.attack_enemy()

"""
1- classes & objects
2- inheritance
3- encapsulation
4- abstraction
5- polymorphism
"""