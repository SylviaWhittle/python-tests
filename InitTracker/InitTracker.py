from ast import parse
from operator import indexOf
import os
from colorama import Fore, Back, Style

# Init colorama
#init()

clear = lambda: os.system('cls')

class Combatant:
    
    def __init__(self, name, initiative):
        self.name = name
        self.init = initiative
        self.hp = None
        self.maxhp = None
        self.ac = None

    def __str__(self):
        attributeString = ''

        attributeString += self.name
        attributeString += Fore.LIGHTBLACK_EX + f' {self.init} ' + Fore.WHITE + '|'
        if self.hp != None:
            color = Fore.GREEN
            if self.hp / self.maxhp < 0.5: 
                color = Fore.YELLOW
            if self.hp <= 0:
                color = Fore.RED
            attributeString += color + f'hp: {self.hp}/{self.maxhp}' + Fore.WHITE + '|'
        if self.ac != None:
            attributeString += Fore.CYAN + f'ac: {self.ac}' + Fore.WHITE + '|'

        return f'{attributeString}'


combatants = []

def parseCommand(split_inp):
    global combatants

    match command:
        case 'add':
            try:
                name = split_inp[1]
                if any(x.name == name for x in combatants):
                    name += str(sum(name in x.name for x in combatants) + 1) 

                init = split_inp[2]

                newCombatant = Combatant(name, int(init))

                args = split_inp[3:]

                for arg in args:
                    split_arg = arg.split(':')
                    
                    attribute = split_arg[0]
                    value = split_arg[1]

                    # Add the new attribute
                    setattr(newCombatant, attribute, int(value))

                    if attribute == 'hp':
                        setattr(newCombatant, 'maxhp', int(value))

                combatants.append(newCombatant)
            except:
                print("that didn't work :c")
            
        case 'remove':
            try:
                name = split_inp[1]
                if any(x.name == name for x in combatants):
                    combatant = next((x for x in combatants if x.name == name), None)
                    combatants.remove(combatant)
                else: print(f'no combatant named: {name}')
            except:
                print("that didn't work :c")

        case 'damage': 
            try:
                name = split_inp[1]
                dam = int(split_inp[2])
                if any(x.name == name for x in combatants):
                    combatant = next((x for x in combatants if x.name == name), None)
                    combatant.hp -= dam
                else: print(f'no combatant named: {name}')
            except:
                print("that didn't work :c")
                
        
        case _:
            print('command not found')
            return -1



clear()
while True:
    inp = input(Fore.LIGHTBLACK_EX + '>_ ')

    print(Fore.WHITE)

    clear()

    split_inp = inp.split(' ')
    command = split_inp[0]

    parseCommand(split_inp)

    combatants.sort(key=lambda x: int(x.init), reverse=True)
    print('')
    print('combatants:')
    for index, combatant in enumerate(combatants):
        
        print(combatant)
    
    print('')

    

    



