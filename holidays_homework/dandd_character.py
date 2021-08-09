'''
Name: Matteo Lamberti
Date: 31/7/21

For a game of Dungeons & Dragons, each
player starts by generating a character
they can play with. This character has,
among other things, six abilities; strength,
dexterity, constitution, intelligence,
wisdom and charisma. These six abilities
have scores that are determined randomly.
You do this by rolling four 6-sided dice
and record the sum of the largest three dice.
You do this six times, once for each ability.
Your character's initial hitpoints are 10 +
your character's constitution modifier. You
find your character's constitution modifier
by subtracting 10 from your character's
constitution, divide by 2 and round down.
'''

import random

class dandd_character():
    def __init__(self,name):
        self.name=name
        self.strength=0
        self.dexterity=0
        self.constitution=0
        self.intelligence=0
        self.wisdom=0
        self.charisma=0
        self.hitpoints=10
    def build(self):
        values_list=[]
        for _ in range(6):
            dl=dice_roll()
            dl.remove(min(dl))
            val=sum(dl)
            values_list.append(val)
        self.strength=values_list[0]
        self.dexterity=values_list[1]
        self.constitution=values_list[2]
        self.intelligence=values_list[3]
        self.wisdom=values_list[4]
        self.charisma=values_list[5]
        self.hitpoints+=int((self.constitution-10)/2)

def dice_roll():
    dice_list=[random.randint(1, 6),random.randint(1, 6),random.randint(1, 6),random.randint(1, 6)]
    return dice_list

def main():
    character=dandd_character("Bamboo")
    character.build()
    print(f"Strength: {character.strength}")
    print(f"Dexterity: {character.dexterity}")
    print(f"Constitution: {character.constitution}")
    print(f"Intelligence: {character.intelligence}")
    print(f"Wisdom: {character.wisdom}")
    print(f"Charisma: {character.charisma}")
    print(f"Hitpoints: {character.hitpoints}")

if "__main__"==__name__:
    main()
