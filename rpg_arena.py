# The program creates a battle arena for players.
import random

# Character Class
class Character:
    # Constructor
    # __init__ function initializes or adds value to the object attributes
    def __init__(self, name, strength, health, defense):
        self.name = name
        self.strength = strength
        self.health = health
        self.defense = defense

    # takeDamage() Method
    def takeDamage(self, damage):
        damageTaken = damage - self.defense
        self.health -= damageTaken
        return damageTaken

    # attack() Method
    def attack(self, target):
        damage = self.strength * 2
        damageDealt = target.takeDamage(damage)
        return damageDealt

    # isAlive() Method
    def isAlive(self):
        return self.health > 0

# Extend a Class
class Rogue(Character):
    def attack(self, target):
        dexterity = 20
        criticalHit = random.randint(0, 100) < dexterity
        damage = self.strength * 2
        if criticalHit:
            damage *= 2
            print("*** Critical Hit ***")
        damageDealt = target.takeDamage(damage)
        return damageDealt

# Class Objects
player1 = Character("Cheetah", 10, 100, 2)
print(player1.name)
print(player1.strength)
print(player1.health)
print(player1.defense)

player2 = Rogue("Latte", 8, 100, 4)
print(player2.name)
print(player2.strength)
print(player2.health)
print(player2.defense)


# Create arena battle
print(player1.name + " vs. " + player2.name)
print(str(player1.health) + " vs. " + str(player2.health))

while player1.isAlive() and player2.isAlive():
    print(player1.name + ": " + str(player1.health))
    print(player2.name + ": " + str(player2.health))

    damage = player1.attack(player2)
    print(player1.name + " hits " + player2.name + " for " + str(damage))

    damage = player2.attack(player1)
    print(player2.name + " hits " + player1.name + " for " + str(damage))

if player1.isAlive():
    print(player1.name + " health: " + str(player1.health) + " wins!")
elif player2.isAlive():
    print(player2.name + " health: " + str(player2.health) + " wins!")
else:
    print("It's a draw!")