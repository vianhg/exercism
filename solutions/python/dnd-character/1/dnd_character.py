import random
import math

class Character:
    '''Character class'''
    def __init__(self):
        '''Init stats'''
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        # hitpoints are 10 + your character's constitution
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        ''' Throw the dice 4 times, discard the min value and return the sum of the rest of values'''
        attempts = [random.randint(1, 6) for idx in range(4)]
        return sum(attempts) - min(attempts)
    

def modifier(value):
    '''Calculates the value of constitution modified by substracting 10, dividing by 2 and floor'''
    return math.floor((value - 10)/2)
