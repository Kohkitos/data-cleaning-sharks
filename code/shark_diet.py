import pandas as pd
import numpy as np

data = pd.read_csv('../src/shark_diet.csv')
data.set_index('Species', inplace=True)

species = input('What shark are you looking for? ').capitalize()

if 'shark' in species:
    species = species.strip('shark').strip(' ')

print('-' * 15)

try:
    food = data.loc[species]['Food Preference']
    snacker = data.loc[species]['Kind of Snacker']
    
    if '[' in food:
        food = food.strip("[]").replace("'", "").split()
        
    if '[' in snacker:
        snacker = snacker.strip("[]").split(", ")
        snacker = [e.strip("'") for e in snacker]
    
    print(f'{species} sharks like their food when they are ', end='')
    
    if type(food) == str:
        print(f'{food} and they are scientificly consiedered ', end='')
        
    else:
        for i in range(len(food)):
            print(f'{food[i]} ', end='')
            if i == len(food) - 3:
                print(', ', end='')
            elif i == len(food) - 2:
                print('and ', end='')
            else:
                print('and they are scientificly consiedered ', end='')
    
    if type(snacker) == str:
        print(f'{snacker}.')
        
    else:
        for i in range(len(snacker)):
            print(f'{snacker[i]}s', end='')
            if i == len(snacker) - 3:
                print(' , others are considered ', end='')
            elif i == len(snacker) -2:
                print(' and others are considered ', end='')
            else:
                print('.')

except:
    while True:
        confirmation = input("We didn't recognize that shark, would you like to add information about it? [Y/N] ").lower()
        if (confirmation == 'y') | (confirmation == 'n'):
            break
        else:
            print('Please, enter "y" or "n".')
    
    if confirmation == 'y':
        food = input('What do they like to eat? ').capitalize()
        snacker = input('In the scientific methodology of cataloguing sharks as snackers, what are they considered? ')
        row = {'Food Preference': food, 'Kind of Snacker': snacker}
        row = pd.Series(row)
        row.name = species
        data = data.append(row)
        
        print('-' * 7 + 'Loading' + '-' * 7)
        try:
            data.to_csv('../src/shark_diet.csv')
            print('Data Saved.')
        except:
            print("There was an error, data couldn't be saved")
            
    else:
        print('OK.')