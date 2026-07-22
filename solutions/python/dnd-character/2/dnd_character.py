''' Character for D&D'''
import random
import math

class Character:
    '''Character class'''
    def __init__(self):
        '''Init stats'''
        self.strength = Character.ability()
        self.dexterity = Character.ability()
        self.constitution = Character.ability()
        self.intelligence = Character.ability()
        self.wisdom = Character.ability()
        self.charisma = Character.ability()
        # hitpoints are 10 + your character's constitution
        self.hitpoints = 10 + modifier(self.constitution)

    @staticmethod
    def ability():
        ''' Throw the dice 4 times, discard the min value and return the sum of the rest of values'''
        attempts = [random.randint(1, 6) for idx in range(4)]
        return sum(attempts) - min(attempts)
    

def modifier(value):
    '''Calculates the value of constitution modified by substracting 10, dividing by 2 and floor'''
    return math.floor((value - 10)/2)
