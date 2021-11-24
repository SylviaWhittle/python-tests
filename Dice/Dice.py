# %% DICE
import numpy as np
import matplotlib.pyplot as plt
from random import randrange
import logging

from numpy.random.mtrand import randint
# import seaborn as sns
# import pandas

# Error logging
level = logging.DEBUG
fmt = '[%(levelname)s] %(asctime)s - %(message)s'
logging.basicConfig(level=level, format=fmt)

logging.info('Done!')


#%% 

# Stats for rolling a die:
# Probability distribution normalised
# Max and min

class Die:
    def __init__(self, max):
        self.max = int(max)
        self.min = 1
        self.total = 0
        self.values = []
        self.name = f'd{self.max}'
        for i in range(self.min, self.max + 1):
            self.values.append(i)
            self.total = self.total + i
        self.average = self.total / len(self.values)
    
    def stats(self):
        print(self.min)
        print(self.max)
        print(self.values)
        print(self.total)
        print(self.average)

def Combination_List(dice):

    dicevals = np.ones(len(dice))
    combination_list = []
    finished = False
    while True:
        combination = []
        for index in dicevals:
            combination.append(index)
        combination_list.append(tuple(combination))

        # Increment
        for dieIndex, val in enumerate(dicevals):
            if(dicevals[dieIndex] < dice[dieIndex].max):
                dicevals[dieIndex] += 1
                break
            else:
                dicevals[dieIndex] = dice[dieIndex].min
                if(dieIndex == len(dicevals) - 1):
                    finished = True

        if(finished): break
        
    return combination_list


def DiceStats(dicestr, normalize=False):

    dice = parseDice(dicestr)

    combination_list = Combination_List(dice)
    print(combination_list)

    sums = []
    frequencies = []

    for tuple in combination_list:
        sum = 0
        for val in tuple:
            sum += val
        
        if sum in sums:
            frequencies[sums.index(sum)] += 1
        else:
            sums.append(sum)
            frequencies.append(1)

    # Normalise
    if(normalize):
        total = 0
        for i, val in enumerate(frequencies):
            total += val
        
        for i, val in enumerate(frequencies):
            frequencies[i] = val/total

    # Create title
    title = ''
    for index, die in enumerate(dice):
        title += die.name + ' '
        if(index < len(dice) - 1):
            title += '+ '
        

    plt.bar(sums, frequencies)
    plt.xticks(sums)
    plt.title(title)
    plt.show()


def Roll(dicestr):
    
    dice = parseDice(dicestr)

    result = 0
    for die in dice:
        result += randrange(die.min, die.max + 1)

    return result
    

def parseDice(dicestr):
    splitmainstr = dicestr.split(' ')
    dice = []

    for string in splitmainstr:
        splitstr = string.split('d')
        if(splitstr[0] == ''):
            count = 1
        else: 
            count = int(splitstr[0])
        
        dieval = splitstr[1]

        for i in range(count):
            dice.append(Die(dieval))

    return dice

        
dicestr = '1d4 2d6'
DiceStats(dicestr, False)
Roll(dicestr)
